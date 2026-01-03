import axios from 'axios';

const API_BASE = 'http://localhost:3001/api';

export async function analyzeImage(base64: string) {
    try {
        const response = await axios.post(`${API_BASE}/analyze`, {
            image: base64,
        });
        return response.data;
    } catch (error: any) {
        console.error('API Error:', error);
        throw error;
    }
}

export async function sendChatMessage(message: string, history: any[] = []) {
    try {
        const response = await axios.post(`${API_BASE}/chat`, {
            message,
            history,
        });
        return response.data;
    } catch (error: any) {
        console.error('Chat API Error:', error);
        throw error;
    }
}
