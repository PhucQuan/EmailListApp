// Express server using direct REST API calls to Gemini
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import bodyParser from "body-parser";

dotenv.config();
const app = express();
app.use(cors());
app.use(bodyParser.json({ limit: "15mb" }));

const PORT = process.env.PORT || 3001;
const API_KEY = process.env.GEMINI_API_KEY;

if (!API_KEY) {
    console.warn("⚠️  WARNING: GEMINI_API_KEY not set. Please set it in .env file");
}

const ANALYSIS_PROMPT = `You are an expert cosmetic chemist and safety reviewer.

Input: an image of a product's ingredient list (INCI). Extract ingredients, normalize names, and return only a JSON object with EXACT fields:
{
  "product_name": "...",
  "product_type": "cleanser|moisturizer|serum|sunscreen|toner|mask|other",
  "ingredients_raw": ["..."],
  "ingredients_analyzed": [
    {
      "name":"", 
      "function":"", 
      "function_vi": "Mô tả công dụng bằng tiếng Việt, ngắn gọn dễ hiểu",
      "safety_level":"safe|low_risk|watch|avoid", 
      "comedogenic_rating":0-5,
      "comedogenic_warning": true/false,
      "uncertain":false
    }
  ],
  "top_ingredients": ["5-7 thành phần đầu tiên (nồng độ cao nhất)"],
  "notable_ingredients": ["..."],
  "suitable_for_skin_types": ["normal", "oily", "dry", "combination", "sensitive", "acne-prone"],
  "pros": ["..."],
  "cons": ["..."],
  "warnings": ["..."],
  "ingredient_interactions": {
    "retinol": "Có thể dùng chung / Không nên dùng chung / Không liên quan",
    "aha_bha": "Có thể dùng chung / Không nên dùng chung / Không liên quan",
    "vitamin_c": "Có thể dùng chung / Không nên dùng chung / Không liên quan",
    "benzoyl_peroxide": "Có thể dùng chung / Không nên dùng chung / Không liên quan",
    "niacinamide": "Có thể dùng chung / Không nên dùng chung / Không liên quan"
  },
  "overall_assessment": {
    "strengths": ["Điểm mạnh 1", "Điểm mạnh 2"],
    "usage_notes": ["Lưu ý 1", "Lưu ý 2"]
  },
  "recommendation_score": 0-100
}

Rules:
- Do not include extra prose. Output valid JSON only.
- For function_vi, write in Vietnamese, simple and easy to understand (e.g., "Dưỡng ẩm cho da", "Chống oxy hóa").
- For top_ingredients, list the first 5-7 ingredients (highest concentration).
- Set comedogenic_warning to true if comedogenic_rating >= 3 (high risk).
- In suitable_for_skin_types, list ALL skin types this product is good for based on ingredients.
- For ingredient_interactions, analyze if this product can be safely combined with each common active.
- If a name is unclear, set uncertain:true for that ingredient.
- For warnings, include ingredient-specific concerns (e.g., "Chứa hương liệu - có thể kích ứng da nhạy cảm").
- Rate comedogenic 0-5 (0 = non-comedogenic, 3-5 = high risk for acne).
- recommendation_score is 0 (avoid) to 100 (very safe/good).
- Extract ALL ingredients in order from the image.
- Use proper INCI nomenclature.
- Be thorough but concise in pros/cons.
- Pros should highlight beneficial ingredients and their effects.
- Cons should mention potentially problematic ingredients.
- In overall_assessment.strengths, list 2-3 key benefits of this product.
- In overall_assessment.usage_notes, list 2-3 important usage tips or precautions.`;

app.post("/analyze", async (req, res) => {
    try {
        const { imageBase64 } = req.body;
        if (!imageBase64) {
            return res.status(400).json({ error: "imageBase64 required" });
        }

        console.log("📸 Analyzing image with Gemini AI...");

        // Prepare image data (remove data URL prefix if present)
        const base64Data = imageBase64.replace(/^data:image\/\w+;base64,/, "");

        // Detect mime type
        let mimeType = "image/png";
        if (imageBase64.includes("data:image/jpeg") || imageBase64.includes("data:image/jpg")) {
            mimeType = "image/jpeg";
        } else if (imageBase64.includes("data:image/webp")) {
            mimeType = "image/webp";
        }

        // Use v1beta API with gemini-2.5-flash (available in your project)
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`;

        const requestBody = {
            contents: [{
                parts: [
                    { text: ANALYSIS_PROMPT },
                    {
                        inline_data: {
                            mime_type: mimeType,
                            data: base64Data
                        }
                    }
                ]
            }]
        };

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            const errorData = await response.text();
            console.error("API Error:", errorData);
            throw new Error(`API returned ${response.status}: ${errorData}`);
        }

        const data = await response.json();
        console.log("✅ Received response from Gemini");

        // Extract text from response
        const text = data.candidates?.[0]?.content?.parts?.[0]?.text || "";

        if (!text) {
            throw new Error("No text in response");
        }

        // Parse JSON from response
        let parsed;
        try {
            parsed = JSON.parse(text);
        } catch (e) {
            // Try to extract JSON from markdown code blocks
            const jsonMatch = text.match(/```json\s*([\s\S]*?)\s*```/) || text.match(/\{[\s\S]*\}/);
            if (jsonMatch) {
                const jsonStr = jsonMatch[1] || jsonMatch[0];
                parsed = JSON.parse(jsonStr);
            } else {
                console.error("Failed to parse JSON from response:", text);
                return res.status(500).json({
                    ok: false,
                    error: "Failed to parse AI response",
                    raw: text
                });
            }
        }

        res.json({ ok: true, result: parsed });
    } catch (err) {
        console.error("❌ Error:", err);
        res.status(500).json({ ok: false, error: err.message });
    }
});

// Health check endpoint
app.get("/health", (req, res) => {
    res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// ============= AI CHAT ENDPOINT =============
const CHAT_SYSTEM_PROMPT = `Bạn là SkinLab AI - một trợ lý tư vấn mỹ phẩm và chăm sóc da chuyên nghiệp.

ROLE: Bạn đóng vai như một bác sĩ da liễu thân thiện, cung cấp lời khuyên về:
- Thành phần mỹ phẩm (INCI names, công dụng, độ an toàn)
- Chăm sóc da theo loại da (da dầu, da khô, da nhạy cảm, da hỗn hợp, da mụn)
- Các vấn đề da liễu phổ biến (mụn, thâm, nám, lão hóa, khô da)
- Cách kết hợp sản phẩm skincare
- Routine chăm sóc da sáng/tối
- ĐỀ XUẤT SẢN PHẨM CỤ THỂ phù hợp với loại da và vấn đề của người dùng

KHI ĐỀ XUẤT SẢN PHẨM:
- Gợi ý 2-3 sản phẩm CỤ THỂ từ các thương hiệu phổ biến (La Roche-Posay, CeraVe, The Ordinary, Paula's Choice, Some By Mi, Cosrx, Innisfree, Klairs, Neutrogena, Cetaphil, v.v.)
- Giải thích TẠI SAO sản phẩm đó phù hợp (thành phần chính, công dụng)
- Gợi ý cả sản phẩm bình dân và cao cấp nếu có thể
- Nêu rõ giá tham khảo nếu biết

VÍ DỤ ĐỀ XUẤT:
"Với da dầu mụn, mình gợi ý:
• CeraVe Foaming Cleanser - sữa rửa mặt không xà phòng, có Niacinamide
• Paula's Choice 2% BHA - tẩy tế bào chết, thông thoáng lỗ chân lông
• La Roche-Posay Effaclar Duo+ - dưỡng ẩm kiềm dầu, giảm mụn"

GUIDELINES:
1. Trả lời bằng ngôn ngữ mà người dùng sử dụng (Tiếng Việt, English, hoặc Français)
2. Giải thích đơn giản, dễ hiểu, tránh thuật ngữ quá chuyên môn
3. Khi được hỏi recommend sản phẩm, HÃY ĐỀ XUẤT SẢN PHẨM CỤ THỂ kèm lý do
4. Ở cuối tin nhắn, nhắc nhẹ: "💡 Đây chỉ là gợi ý tham khảo nhé!"
5. Sử dụng emoji phù hợp để thân thiện hơn

QUAN TRỌNG - FORMAT VĂN BẢN:
- KHÔNG sử dụng markdown như **bold**, *italic*, # headers
- Dùng bullet points với dấu • hoặc - 
- Xuống dòng để dễ đọc
- Trả lời ngắn gọn, tối đa 4-5 đoạn văn`;


// Store conversation history per session (in-memory, resets on server restart)
const conversations = new Map();

app.post("/chat", async (req, res) => {
    try {
        const { message, sessionId = 'default' } = req.body;

        if (!message) {
            return res.status(400).json({ ok: false, error: "Message is required" });
        }

        console.log(`💬 Chat message from session ${sessionId}: ${message.substring(0, 50)}...`);

        // Get or create conversation history
        if (!conversations.has(sessionId)) {
            conversations.set(sessionId, []);
        }
        const history = conversations.get(sessionId);

        // Build conversation context
        const conversationContext = history.map(msg =>
            `${msg.role === 'user' ? 'User' : 'Assistant'}: ${msg.content}`
        ).join('\n');

        const fullPrompt = conversationContext
            ? `${conversationContext}\n\nUser: ${message}\n\nAssistant:`
            : `User: ${message}\n\nAssistant:`;

        // Call Gemini API
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`;

        const requestBody = {
            contents: [{
                parts: [{ text: CHAT_SYSTEM_PROMPT + '\n\n' + fullPrompt }]
            }],
            generationConfig: {
                temperature: 0.7,
                maxOutputTokens: 1024,
            }
        };

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            const errorData = await response.text();
            console.error("Chat API Error:", errorData);
            throw new Error(`API returned ${response.status}`);
        }

        const data = await response.json();
        const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "Xin lỗi, tôi không thể trả lời câu hỏi này.";

        // Update conversation history (keep last 10 exchanges)
        history.push({ role: 'user', content: message });
        history.push({ role: 'assistant', content: reply });
        if (history.length > 20) {
            history.splice(0, 2); // Remove oldest exchange
        }

        console.log("✅ Chat response sent");
        res.json({ ok: true, reply });

    } catch (err) {
        console.error("❌ Chat Error:", err);
        res.status(500).json({ ok: false, error: err.message });
    }
});

// Clear chat history endpoint
app.post("/chat/clear", (req, res) => {
    const { sessionId = 'default' } = req.body;
    conversations.delete(sessionId);
    res.json({ ok: true, message: "Conversation cleared" });
});

app.listen(PORT, () => {
    console.log(`🚀 Server listening on http://localhost:${PORT}`);
    console.log(`📡 API endpoints:`);
    console.log(`   - POST /analyze (image analysis)`);
    console.log(`   - POST /chat (AI chat)`);
    console.log(`🤖 Using model: gemini-2.5-flash`);
});
