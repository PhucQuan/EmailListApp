// i18n configuration with Vietnamese, English, and French
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

// Translation resources
const resources = {
    vi: {
        translation: {
            // Navigation
            nav: {
                home: 'Trang chủ',
                analyze: 'Phân tích',
                knowledge: 'Kiến thức',
                about: 'Giới thiệu',
            },
            // Home page (legacy)
            home: {
                hero: {
                    title: 'Giải mã thành phần mỹ phẩm với AI',
                    subtitle: 'Phân tích thông minh, an toàn cho làn da của bạn',
                    cta: 'Phân tích ngay',
                },
                features: {
                    title: 'Tính năng nổi bật',
                    scan: {
                        title: 'Nhận diện qua ảnh',
                        desc: 'Chỉ cần chụp ảnh bảng thành phần, AI sẽ tự động nhận diện',
                    },
                    analyze: {
                        title: 'Phân tích chuyên sâu',
                        desc: 'Đánh giá độ an toàn, công dụng từng thành phần',
                    },
                    instant: {
                        title: 'Kết quả tức thì',
                        desc: 'Nhận kết quả trong vài giây với công nghệ AI tiên tiến',
                    },
                    recommend: {
                        title: 'Gợi ý thông minh',
                        desc: 'Tư vấn phù hợp theo từng loại da',
                    },
                },
                howItWorks: {
                    title: 'Cách hoạt động',
                    step1: {
                        title: 'Chụp ảnh',
                        desc: 'Chụp ảnh rõ nét bảng thành phần sản phẩm',
                    },
                    step2: {
                        title: 'Upload',
                        desc: 'Tải ảnh lên hệ thống phân tích',
                    },
                    step3: {
                        title: 'Nhận kết quả',
                        desc: 'Xem báo cáo phân tích chi tiết',
                    },
                },
                cta: {
                    title: 'Sẵn sàng khám phá?',
                    subtitle: 'Bắt đầu phân tích mỹ phẩm của bạn ngay hôm nay',
                    button: 'Bắt đầu miễn phí',
                },
            },
            // Home page new
            homePage: {
                hero: {
                    title1: 'Hiểu rõ',
                    highlight: 'thành phần mỹ phẩm',
                    title2: 'bạn đang dùng',
                    subtitle: 'Chụp ảnh bảng thành phần, AI sẽ phân tích độ an toàn và đưa ra khuyến nghị phù hợp với làn da của bạn.',
                    cta: 'Phân tích ngay',
                },
                stats: {
                    ingredients: 'Thành phần đã phân tích',
                    brands: 'Thương hiệu hỗ trợ',
                    accuracy: 'Độ chính xác AI',
                },
                features: {
                    title: 'Tại sao chọn SkinLab AI?',
                    subtitle: 'Công nghệ AI tiên tiến giúp bạn đọc hiểu thành phần mỹ phẩm một cách dễ dàng',
                    smart: {
                        title: 'Nhận diện thông minh',
                        desc: 'Chụp ảnh bảng thành phần, AI sẽ tự động đọc và phân tích từng ingredient.',
                    },
                    safety: {
                        title: 'Đánh giá an toàn',
                        desc: 'Mỗi thành phần được đánh giá độ an toàn, khả năng gây mụn, và phù hợp loại da.',
                    },
                    instant: {
                        title: 'Kết quả tức thì',
                        desc: 'Nhận báo cáo chi tiết trong vài giây với công nghệ AI tiên tiến.',
                    },
                    chat: {
                        title: 'Tư vấn AI',
                        desc: 'Chat trực tiếp với AI để được tư vấn skincare routine phù hợp.',
                    },
                },
                howItWorks: {
                    title: 'Cách hoạt động',
                    subtitle: 'Chỉ 3 bước đơn giản để hiểu rõ sản phẩm bạn đang dùng',
                },
                steps: {
                    step1: { title: 'Chụp ảnh', desc: 'Chụp rõ nét bảng thành phần trên sản phẩm' },
                    step2: { title: 'Phân tích', desc: 'AI đọc và phân tích từng thành phần' },
                    step3: { title: 'Đánh giá', desc: 'Nhận điểm số và khuyến nghị chi tiết' },
                },
                testimonials: {
                    title: 'Người dùng nói gì?',
                    t1: {
                        quote: 'Cuối cùng cũng hiểu được mấy cái tên lạ hoắc trên chai sữa rửa mặt của mình!',
                        role: 'Da dầu mụn',
                    },
                    t2: {
                        quote: 'App giúp mình tránh được mấy sản phẩm có thành phần gây kích ứng cho da nhạy cảm.',
                        role: 'Da nhạy cảm',
                    },
                    t3: {
                        quote: 'Tiết kiệm được bao nhiêu tiền nhờ check thành phần trước khi mua!',
                        role: 'Skincare enthusiast',
                    },
                },
                cta: {
                    title: 'Bắt đầu phân tích miễn phí',
                    subtitle: 'Không cần đăng ký, không giới hạn số lần sử dụng. Chỉ cần upload ảnh và nhận kết quả.',
                    button: 'Thử ngay',
                },
            },
            // Analyzer page
            analyzer: {
                title: 'Phân tích thành phần',
                subtitle: 'Upload ảnh bảng thành phần để nhận kết quả phân tích chi tiết',
                upload: {
                    title: 'Upload ảnh',
                    button: 'Chọn ảnh',
                    camera: 'Dùng camera',
                    dragDrop: 'hoặc kéo thả ảnh vào đây',
                    tips: {
                        title: 'Mẹo để có kết quả tốt nhất',
                        tip1: 'Đảm bảo ánh sáng đủ và rõ nét',
                        tip2: 'Chụp toàn bộ danh sách thành phần',
                        tip3: 'Tránh bóng đổ và phản chiếu',
                        tip4: 'Giữ văn bản nằm ngang',
                    },
                },
                analyzing: 'Đang phân tích với AI...',
                error: {
                    title: 'Phân tích thất bại',
                },
                result: {
                    title: 'Kết quả phân tích',
                    points: 'điểm',
                    score: 'Điểm đánh giá',
                    scoreDesc: 'Mức độ an toàn và chất lượng tổng thể',
                    topIngredients: 'Thành phần chính (nồng độ cao nhất)',
                    suitableFor: 'Phù hợp cho',
                    strengths: 'Điểm mạnh',
                    usageNotes: 'Lưu ý khi sử dụng',
                    interactions: 'Tương tác với hoạt chất phổ biến',
                    pros: 'Ưu điểm',
                    cons: 'Nhược điểm',
                    warnings: 'Cảnh báo',
                    notable: 'Thành phần nổi bật',
                    fullList: 'Danh sách đầy đủ thành phần',
                    ingredients: 'thành phần',
                    ingredient: 'Thành phần',
                    function: 'Công dụng',
                    safety: 'An toàn',
                    comedogenic: 'Gây mụn',
                },
            },
            lang: 'vi',
            // Knowledge page
            knowledge: {
                title: 'Kiến thức làm đẹp',
                subtitle: 'Tìm hiểu về thành phần mỹ phẩm và cách chăm sóc da',
                dictionary: {
                    title: 'Từ điển thành phần',
                    desc: 'Tra cứu các thành phần phổ biến trong mỹ phẩm',
                },
                guide: {
                    title: 'Hướng dẫn đọc INCI',
                    desc: 'Cách đọc và hiểu danh sách thành phần sản phẩm',
                },
                tips: {
                    title: 'Tips chăm sóc da',
                    desc: 'Các mẹo chăm sóc da theo từng loại da',
                },
                faq: {
                    title: 'Câu hỏi thường gặp',
                    desc: 'Giải đáp thắc mắc về thành phần mỹ phẩm',
                },
            },
            // About page
            about: {
                title: 'Về SkinLab AI',
                subtitle: 'Giải pháp phân tích mỹ phẩm thông minh',
                mission: {
                    title: 'Sứ mệnh',
                    desc: 'Giúp mọi người hiểu rõ hơn về thành phần mỹ phẩm, đưa ra quyết định sáng suốt cho làn da của mình.',
                },
                tech: {
                    title: 'Công nghệ',
                    desc: 'Sử dụng Google Gemini AI - mô hình AI tiên tiến nhất để phân tích và đánh giá thành phần mỹ phẩm.',
                },
                disclaimer: {
                    title: 'Lưu ý quan trọng',
                    desc: 'Thông tin được cung cấp chỉ mang tính chất tham khảo. Không thay thế cho tư vấn y khoa chuyên nghiệp. Nếu bạn có vấn đề về da, hãy tham khảo ý kiến bác sĩ da liễu.',
                },
            },
            // Common
            common: {
                learnMore: 'Tìm hiểu thêm',
                getStarted: 'Bắt đầu',
                loading: 'Đang tải...',
                error: 'Đã xảy ra lỗi',
                retry: 'Thử lại',
            },
            // Footer
            footer: {
                tagline: 'Giải mã mỹ phẩm với AI',
                links: 'Liên kết',
                contact: 'Liên hệ',
                rights: 'Đã đăng ký bản quyền',
                disclaimer: 'Chỉ mang tính tham khảo',
            },
            // Skin types
            skinTypes: {
                normal: 'Da thường',
                oily: 'Da dầu',
                dry: 'Da khô',
                combination: 'Da hỗn hợp',
                sensitive: 'Da nhạy cảm',
                'acne-prone': 'Da mụn',
            },
        },
    },
    en: {
        translation: {
            nav: {
                home: 'Home',
                analyze: 'Analyze',
                knowledge: 'Knowledge',
                about: 'About',
            },
            home: {
                hero: {
                    title: 'Decode Cosmetic Ingredients with AI',
                    subtitle: 'Smart analysis for your skin safety',
                    cta: 'Analyze Now',
                },
                features: {
                    title: 'Key Features',
                    scan: {
                        title: 'Photo Recognition',
                        desc: 'Just take a photo of ingredients, AI will recognize automatically',
                    },
                    analyze: {
                        title: 'Deep Analysis',
                        desc: 'Safety rating and function for each ingredient',
                    },
                    instant: {
                        title: 'Instant Results',
                        desc: 'Get results in seconds with advanced AI',
                    },
                    recommend: {
                        title: 'Smart Recommendations',
                        desc: 'Personalized advice for your skin type',
                    },
                },
                howItWorks: {
                    title: 'How It Works',
                    step1: {
                        title: 'Take Photo',
                        desc: 'Capture a clear photo of product ingredients',
                    },
                    step2: {
                        title: 'Upload',
                        desc: 'Upload the image for analysis',
                    },
                    step3: {
                        title: 'Get Results',
                        desc: 'View detailed analysis report',
                    },
                },
                cta: {
                    title: 'Ready to explore?',
                    subtitle: 'Start analyzing your cosmetics today',
                    button: 'Get Started Free',
                },
            },
            homePage: {
                hero: {
                    title1: 'Understand',
                    highlight: 'cosmetic ingredients',
                    title2: 'you are using',
                    subtitle: 'Take a photo of the ingredient list, AI will analyze safety and provide recommendations for your skin.',
                    cta: 'Analyze Now',
                },
                stats: {
                    ingredients: 'Ingredients analyzed',
                    brands: 'Brands supported',
                    accuracy: 'AI accuracy',
                },
                features: {
                    title: 'Why choose SkinLab AI?',
                    subtitle: 'Advanced AI technology helps you understand cosmetic ingredients easily',
                    smart: {
                        title: 'Smart Recognition',
                        desc: 'Take a photo of ingredients, AI will automatically read and analyze each one.',
                    },
                    safety: {
                        title: 'Safety Rating',
                        desc: 'Each ingredient is rated for safety, comedogenicity, and skin type compatibility.',
                    },
                    instant: {
                        title: 'Instant Results',
                        desc: 'Get detailed reports in seconds with advanced AI technology.',
                    },
                    chat: {
                        title: 'AI Consultation',
                        desc: 'Chat directly with AI for personalized skincare routine advice.',
                    },
                },
                howItWorks: {
                    title: 'How It Works',
                    subtitle: 'Just 3 simple steps to understand your products',
                },
                steps: {
                    step1: { title: 'Take Photo', desc: 'Capture a clear photo of the ingredient list' },
                    step2: { title: 'Analyze', desc: 'AI reads and analyzes each ingredient' },
                    step3: { title: 'Get Results', desc: 'Receive scores and detailed recommendations' },
                },
                testimonials: {
                    title: 'What users say?',
                    t1: {
                        quote: 'Finally understand those weird names on my face wash bottle!',
                        role: 'Oily acne-prone skin',
                    },
                    t2: {
                        quote: 'The app helped me avoid products with ingredients that irritate my sensitive skin.',
                        role: 'Sensitive skin',
                    },
                    t3: {
                        quote: 'Saved so much money by checking ingredients before buying!',
                        role: 'Skincare enthusiast',
                    },
                },
                cta: {
                    title: 'Start analyzing for free',
                    subtitle: 'No registration required, unlimited uses. Just upload a photo and get results.',
                    button: 'Try Now',
                },
            },
            analyzer: {
                title: 'Ingredient Analysis',
                subtitle: 'Upload an ingredient list photo for detailed analysis',
                upload: {
                    title: 'Upload Photo',
                    button: 'Choose Photo',
                    camera: 'Use Camera',
                    dragDrop: 'or drag and drop here',
                    tips: {
                        title: 'Tips for best results',
                        tip1: 'Ensure good lighting and focus',
                        tip2: 'Capture the entire ingredient list',
                        tip3: 'Avoid shadows and reflections',
                        tip4: 'Keep text horizontal',
                    },
                },
                analyzing: 'Analyzing with AI...',
                error: {
                    title: 'Analysis Failed',
                },
                result: {
                    title: 'Analysis Result',
                    points: 'points',
                    score: 'Rating Score',
                    scoreDesc: 'Overall safety and quality rating',
                    topIngredients: 'Top Ingredients (Highest Concentration)',
                    suitableFor: 'Suitable For',
                    strengths: 'Strengths',
                    usageNotes: 'Usage Notes',
                    interactions: 'Interactions with Common Actives',
                    pros: 'Pros',
                    cons: 'Cons',
                    warnings: 'Warnings',
                    notable: 'Notable Ingredients',
                    fullList: 'Full Ingredient List',
                    ingredients: 'ingredients',
                    ingredient: 'Ingredient',
                    function: 'Function',
                    safety: 'Safety',
                    comedogenic: 'Comedogenic',
                },
            },
            lang: 'en',
            knowledge: {
                title: 'Beauty Knowledge',
                subtitle: 'Learn about cosmetic ingredients and skincare',
                dictionary: {
                    title: 'Ingredient Dictionary',
                    desc: 'Look up common cosmetic ingredients',
                },
                guide: {
                    title: 'INCI Reading Guide',
                    desc: 'How to read and understand product ingredient lists',
                },
                tips: {
                    title: 'Skincare Tips',
                    desc: 'Skincare tips for different skin types',
                },
                faq: {
                    title: 'FAQ',
                    desc: 'Common questions about cosmetic ingredients',
                },
            },
            about: {
                title: 'About SkinLab AI',
                subtitle: 'Smart cosmetic analysis solution',
                mission: {
                    title: 'Mission',
                    desc: 'Help everyone better understand cosmetic ingredients and make informed decisions for their skin.',
                },
                tech: {
                    title: 'Technology',
                    desc: 'Using Google Gemini AI - the most advanced AI model to analyze and evaluate cosmetic ingredients.',
                },
                disclaimer: {
                    title: 'Important Note',
                    desc: 'Information provided is for reference only. This does not replace professional medical advice. If you have skin concerns, please consult a dermatologist.',
                },
            },
            common: {
                learnMore: 'Learn More',
                getStarted: 'Get Started',
                loading: 'Loading...',
                error: 'An error occurred',
                retry: 'Retry',
            },
            footer: {
                tagline: 'Decode cosmetics with AI',
                links: 'Links',
                contact: 'Contact',
                rights: 'All rights reserved',
                disclaimer: 'For reference only',
            },
            skinTypes: {
                normal: 'Normal',
                oily: 'Oily',
                dry: 'Dry',
                combination: 'Combination',
                sensitive: 'Sensitive',
                'acne-prone': 'Acne-prone',
            },
        },
    },
    fr: {
        translation: {
            nav: {
                home: 'Accueil',
                analyze: 'Analyser',
                knowledge: 'Connaissances',
                about: 'À propos',
            },
            home: {
                hero: {
                    title: 'Décoder les ingrédients cosmétiques avec l\'IA',
                    subtitle: 'Analyse intelligente pour la sécurité de votre peau',
                    cta: 'Analyser maintenant',
                },
                features: {
                    title: 'Fonctionnalités clés',
                    scan: {
                        title: 'Reconnaissance photo',
                        desc: 'Prenez une photo des ingrédients, l\'IA les reconnaîtra automatiquement',
                    },
                    analyze: {
                        title: 'Analyse approfondie',
                        desc: 'Évaluation de sécurité et fonction de chaque ingrédient',
                    },
                    instant: {
                        title: 'Résultats instantanés',
                        desc: 'Obtenez des résultats en quelques secondes avec l\'IA avancée',
                    },
                    recommend: {
                        title: 'Recommandations intelligentes',
                        desc: 'Conseils personnalisés pour votre type de peau',
                    },
                },
                howItWorks: {
                    title: 'Comment ça marche',
                    step1: {
                        title: 'Prenez une photo',
                        desc: 'Capturez une photo claire des ingrédients du produit',
                    },
                    step2: {
                        title: 'Téléchargez',
                        desc: 'Téléchargez l\'image pour l\'analyse',
                    },
                    step3: {
                        title: 'Obtenez les résultats',
                        desc: 'Consultez le rapport d\'analyse détaillé',
                    },
                },
                cta: {
                    title: 'Prêt à explorer?',
                    subtitle: 'Commencez à analyser vos cosmétiques dès aujourd\'hui',
                    button: 'Commencer gratuitement',
                },
            },
            homePage: {
                hero: {
                    title1: 'Comprendre',
                    highlight: 'les ingrédients cosmétiques',
                    title2: 'que vous utilisez',
                    subtitle: 'Prenez une photo de la liste des ingrédients, l\'IA analysera la sécurité et fournira des recommandations pour votre peau.',
                    cta: 'Analyser maintenant',
                },
                stats: {
                    ingredients: 'Ingrédients analysés',
                    brands: 'Marques supportées',
                    accuracy: 'Précision IA',
                },
                features: {
                    title: 'Pourquoi choisir SkinLab AI?',
                    subtitle: 'La technologie IA avancée vous aide à comprendre facilement les ingrédients cosmétiques',
                    smart: {
                        title: 'Reconnaissance intelligente',
                        desc: 'Prenez une photo des ingrédients, l\'IA lira et analysera automatiquement chacun d\'eux.',
                    },
                    safety: {
                        title: 'Évaluation de sécurité',
                        desc: 'Chaque ingrédient est évalué pour sa sécurité, sa comédogénicité et sa compatibilité avec le type de peau.',
                    },
                    instant: {
                        title: 'Résultats instantanés',
                        desc: 'Obtenez des rapports détaillés en quelques secondes avec la technologie IA avancée.',
                    },
                    chat: {
                        title: 'Consultation IA',
                        desc: 'Discutez directement avec l\'IA pour des conseils personnalisés de routine de soins.',
                    },
                },
                howItWorks: {
                    title: 'Comment ça marche',
                    subtitle: 'Juste 3 étapes simples pour comprendre vos produits',
                },
                steps: {
                    step1: { title: 'Prenez une photo', desc: 'Capturez une photo claire de la liste des ingrédients' },
                    step2: { title: 'Analyser', desc: 'L\'IA lit et analyse chaque ingrédient' },
                    step3: { title: 'Obtenez les résultats', desc: 'Recevez des scores et des recommandations détaillées' },
                },
                testimonials: {
                    title: 'Que disent les utilisateurs?',
                    t1: {
                        quote: 'J\'ai enfin compris ces noms étranges sur ma bouteille de nettoyant visage!',
                        role: 'Peau grasse à tendance acnéique',
                    },
                    t2: {
                        quote: 'L\'application m\'a aidé à éviter les produits contenant des ingrédients qui irritent ma peau sensible.',
                        role: 'Peau sensible',
                    },
                    t3: {
                        quote: 'J\'ai économisé beaucoup d\'argent en vérifiant les ingrédients avant d\'acheter!',
                        role: 'Passionné de soins',
                    },
                },
                cta: {
                    title: 'Commencez à analyser gratuitement',
                    subtitle: 'Pas d\'inscription requise, utilisation illimitée. Téléchargez simplement une photo et obtenez des résultats.',
                    button: 'Essayer maintenant',
                },
            },
            analyzer: {
                title: 'Analyse des ingrédients',
                subtitle: 'Téléchargez une photo de la liste des ingrédients pour une analyse détaillée',
                upload: {
                    title: 'Télécharger une photo',
                    button: 'Choisir une photo',
                    camera: 'Utiliser l\'appareil photo',
                    dragDrop: 'ou glissez-déposez ici',
                    tips: {
                        title: 'Conseils pour de meilleurs résultats',
                        tip1: 'Assurez un bon éclairage et une bonne mise au point',
                        tip2: 'Capturez toute la liste des ingrédients',
                        tip3: 'Évitez les ombres et les reflets',
                        tip4: 'Gardez le texte horizontal',
                    },
                },
                analyzing: 'Analyse en cours avec l\'IA...',
                error: {
                    title: 'Échec de l\'analyse',
                },
                result: {
                    title: 'Résultat d\'analyse',
                    points: 'points',
                    score: 'Score d\'évaluation',
                    scoreDesc: 'Évaluation globale de sécurité et de qualité',
                    topIngredients: 'Ingrédients principaux (Concentration la plus élevée)',
                    suitableFor: 'Convient pour',
                    strengths: 'Points forts',
                    usageNotes: 'Notes d\'utilisation',
                    interactions: 'Interactions avec les actifs courants',
                    pros: 'Avantages',
                    cons: 'Inconvénients',
                    warnings: 'Avertissements',
                    notable: 'Ingrédients notables',
                    fullList: 'Liste complète des ingrédients',
                    ingredients: 'ingrédients',
                    ingredient: 'Ingrédient',
                    function: 'Fonction',
                    safety: 'Sécurité',
                    comedogenic: 'Comédogène',
                },
            },
            lang: 'fr',
            knowledge: {
                title: 'Connaissances beauté',
                subtitle: 'En savoir plus sur les ingrédients cosmétiques et les soins de la peau',
                dictionary: {
                    title: 'Dictionnaire des ingrédients',
                    desc: 'Recherchez les ingrédients cosmétiques courants',
                },
                guide: {
                    title: 'Guide de lecture INCI',
                    desc: 'Comment lire et comprendre les listes d\'ingrédients',
                },
                tips: {
                    title: 'Conseils soins',
                    desc: 'Conseils pour différents types de peau',
                },
                faq: {
                    title: 'FAQ',
                    desc: 'Questions fréquentes sur les ingrédients cosmétiques',
                },
            },
            about: {
                title: 'À propos de SkinLab AI',
                subtitle: 'Solution d\'analyse cosmétique intelligente',
                mission: {
                    title: 'Mission',
                    desc: 'Aider chacun à mieux comprendre les ingrédients cosmétiques et à prendre des décisions éclairées pour sa peau.',
                },
                tech: {
                    title: 'Technologie',
                    desc: 'Utilisation de Google Gemini AI - le modèle d\'IA le plus avancé pour analyser et évaluer les ingrédients cosmétiques.',
                },
                disclaimer: {
                    title: 'Note importante',
                    desc: 'Les informations fournies sont à titre indicatif uniquement. Cela ne remplace pas les conseils médicaux professionnels. Si vous avez des problèmes de peau, veuillez consulter un dermatologue.',
                },
            },
            common: {
                learnMore: 'En savoir plus',
                getStarted: 'Commencer',
                loading: 'Chargement...',
                error: 'Une erreur est survenue',
                retry: 'Réessayer',
            },
            footer: {
                tagline: 'Décoder les cosmétiques avec l\'IA',
                links: 'Liens',
                contact: 'Contact',
                rights: 'Tous droits réservés',
                disclaimer: 'À titre indicatif uniquement',
            },
            skinTypes: {
                normal: 'Normale',
                oily: 'Grasse',
                dry: 'Sèche',
                combination: 'Mixte',
                sensitive: 'Sensible',
                'acne-prone': 'Acnéique',
            },
        },
    },
};

i18n.use(initReactI18next).init({
    resources,
    lng: 'vi', // Default language
    fallbackLng: 'vi',
    interpolation: {
        escapeValue: false,
    },
});

export default i18n;
