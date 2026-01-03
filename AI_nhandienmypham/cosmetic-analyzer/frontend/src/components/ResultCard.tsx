import { useTranslation } from "react-i18next";

interface ResultCardProps {
    data: any;
}

export default function ResultCard({ data }: ResultCardProps) {
    const { t } = useTranslation();
    const payload = data?.result ? data.result : data;
    const score = payload.recommendation_score ?? 0;

    // Skin type translations
    const getSkinTypeLabel = (type: string) => {
        const labels: Record<string, Record<string, string>> = {
            vi: { normal: "Da thường", oily: "Da dầu", dry: "Da khô", combination: "Da hỗn hợp", sensitive: "Da nhạy cảm", "acne-prone": "Da mụn" },
            en: { normal: "Normal", oily: "Oily", dry: "Dry", combination: "Combination", sensitive: "Sensitive", "acne-prone": "Acne-prone" },
            fr: { normal: "Normale", oily: "Grasse", dry: "Sèche", combination: "Mixte", sensitive: "Sensible", "acne-prone": "Acnéique" }
        };
        const lang = t('lang') === 'vi' ? 'vi' : t('lang') === 'fr' ? 'fr' : 'en';
        return labels[lang]?.[type] || type;
    };

    const interactionLabels: Record<string, string> = {
        "retinol": "Retinol / Tretinoin",
        "aha_bha": "AHA / BHA (Acid)",
        "vitamin_c": "Vitamin C",
        "benzoyl_peroxide": "Benzoyl Peroxide",
        "niacinamide": "Niacinamide"
    };

    // Score color based on value
    const getScoreStyle = (score: number) => {
        if (score >= 80) return { bg: 'bg-green-50 dark:bg-green-900/20', text: 'text-green-600 dark:text-green-400', border: 'border-green-200 dark:border-green-800' };
        if (score >= 60) return { bg: 'bg-blue-50 dark:bg-blue-900/20', text: 'text-blue-600 dark:text-blue-400', border: 'border-blue-200 dark:border-blue-800' };
        if (score >= 40) return { bg: 'bg-yellow-50 dark:bg-yellow-900/20', text: 'text-yellow-600 dark:text-yellow-400', border: 'border-yellow-200 dark:border-yellow-800' };
        return { bg: 'bg-red-50 dark:bg-red-900/20', text: 'text-red-600 dark:text-red-400', border: 'border-red-200 dark:border-red-800' };
    };

    const scoreStyle = getScoreStyle(score);

    // Safety level styling
    const getSafetyStyle = (level: string) => {
        switch (level?.toLowerCase()) {
            case 'safe': return 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400';
            case 'low_risk': return 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400';
            case 'watch': return 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400';
            case 'avoid': return 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400';
            default: return 'bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-400';
        }
    };

    // Comedogenic styling
    const getComedogenicStyle = (rating: number) => {
        if (rating >= 3) return 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400';
        if (rating >= 1) return 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400';
        return 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400';
    };

    // Interaction color
    const getInteractionColor = (status: string) => {
        if (status?.includes('Có thể') || status?.includes('Can') || status?.includes('Peut')) return 'text-green-600 dark:text-green-400';
        if (status?.includes('Không nên') || status?.includes('Avoid') || status?.includes('Éviter')) return 'text-red-600 dark:text-red-400';
        return 'text-gray-500 dark:text-gray-400';
    };

    return (
        <div className="bg-white dark:bg-gray-900 rounded-2xl border border-gray-200 dark:border-gray-800 overflow-hidden">
            {/* Header with Score */}
            <div className="p-6 border-b border-gray-100 dark:border-gray-800">
                <div className="flex items-start justify-between gap-4">
                    <div>
                        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                            {payload.product_name || t('analyzer.result.title')}
                        </h2>
                        {payload.product_type && (
                            <p className="text-gray-500 dark:text-gray-400 mt-1 capitalize">{payload.product_type}</p>
                        )}
                    </div>
                    {/* Score Badge */}
                    <div className={`flex-shrink-0 ${scoreStyle.bg} ${scoreStyle.border} border rounded-2xl px-5 py-3 text-center`}>
                        <div className={`text-3xl font-bold ${scoreStyle.text}`}>{score}</div>
                        <div className="text-xs text-gray-500 dark:text-gray-400">/100 {t('analyzer.result.points')}</div>
                    </div>
                </div>
            </div>

            <div className="p-6 space-y-6">
                {/* Skin Type Suitability */}
                {payload.suitable_for_skin_types && payload.suitable_for_skin_types.length > 0 && (
                    <div>
                        <h3 className="text-sm font-medium text-gray-500 dark:text-gray-400 mb-3 uppercase tracking-wide">
                            {t('analyzer.result.suitableFor')}
                        </h3>
                        <div className="flex flex-wrap gap-2">
                            {payload.suitable_for_skin_types.map((type: string, i: number) => (
                                <span
                                    key={i}
                                    className="px-3 py-1.5 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-400 rounded-lg text-sm"
                                >
                                    {getSkinTypeLabel(type)}
                                </span>
                            ))}
                        </div>
                    </div>
                )}

                {/* Top Ingredients */}
                {payload.top_ingredients && payload.top_ingredients.length > 0 && (
                    <div>
                        <h3 className="text-sm font-medium text-gray-500 dark:text-gray-400 mb-3 uppercase tracking-wide">
                            {t('analyzer.result.topIngredients')}
                        </h3>
                        <div className="flex flex-wrap gap-2">
                            {payload.top_ingredients.map((ing: string, i: number) => (
                                <span
                                    key={i}
                                    className="px-3 py-1.5 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 rounded-lg text-sm"
                                >
                                    {i + 1}. {ing}
                                </span>
                            ))}
                        </div>
                    </div>
                )}

                {/* Pros and Cons Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {/* Pros */}
                    {payload.pros && payload.pros.length > 0 && (
                        <div className="bg-green-50 dark:bg-green-950/20 rounded-xl p-4">
                            <h3 className="font-semibold text-green-800 dark:text-green-300 mb-3 flex items-center gap-2">
                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                                </svg>
                                {t('analyzer.result.pros')}
                            </h3>
                            <ul className="space-y-2">
                                {payload.pros.map((pro: string, i: number) => (
                                    <li key={i} className="text-sm text-green-700 dark:text-green-400 flex items-start gap-2">
                                        <span className="text-green-500 mt-1">•</span>
                                        <span>{pro}</span>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}

                    {/* Cons */}
                    {payload.cons && payload.cons.length > 0 && (
                        <div className="bg-orange-50 dark:bg-orange-950/20 rounded-xl p-4">
                            <h3 className="font-semibold text-orange-800 dark:text-orange-300 mb-3 flex items-center gap-2">
                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                                </svg>
                                {t('analyzer.result.cons')}
                            </h3>
                            <ul className="space-y-2">
                                {payload.cons.map((con: string, i: number) => (
                                    <li key={i} className="text-sm text-orange-700 dark:text-orange-400 flex items-start gap-2">
                                        <span className="text-orange-500 mt-1">•</span>
                                        <span>{con}</span>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>

                {/* Strengths and Usage Notes */}
                {payload.overall_assessment && (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {payload.overall_assessment.strengths && payload.overall_assessment.strengths.length > 0 && (
                            <div className="bg-emerald-50 dark:bg-emerald-950/20 rounded-xl p-4">
                                <h3 className="font-semibold text-emerald-800 dark:text-emerald-300 mb-3 flex items-center gap-2">
                                    💪 {t('analyzer.result.strengths')}
                                </h3>
                                <ul className="space-y-2">
                                    {payload.overall_assessment.strengths.map((item: string, i: number) => (
                                        <li key={i} className="text-sm text-emerald-700 dark:text-emerald-400 flex items-start gap-2">
                                            <span className="text-emerald-500 mt-1">✓</span>
                                            <span>{item}</span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        )}

                        {payload.overall_assessment.usage_notes && payload.overall_assessment.usage_notes.length > 0 && (
                            <div className="bg-amber-50 dark:bg-amber-950/20 rounded-xl p-4">
                                <h3 className="font-semibold text-amber-800 dark:text-amber-300 mb-3 flex items-center gap-2">
                                    📝 {t('analyzer.result.usageNotes')}
                                </h3>
                                <ul className="space-y-2">
                                    {payload.overall_assessment.usage_notes.map((note: string, i: number) => (
                                        <li key={i} className="text-sm text-amber-700 dark:text-amber-400 flex items-start gap-2">
                                            <span className="text-amber-500 mt-1">→</span>
                                            <span>{note}</span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        )}
                    </div>
                )}

                {/* Ingredient Interactions */}
                {payload.ingredient_interactions && typeof payload.ingredient_interactions === 'object' && (
                    <div className="bg-yellow-50 dark:bg-yellow-950/20 rounded-xl p-4">
                        <h3 className="font-semibold text-yellow-800 dark:text-yellow-300 mb-4 flex items-center gap-2">
                            ⚡ {t('analyzer.result.interactions')}
                        </h3>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                            {Object.entries(payload.ingredient_interactions).map(([key, value]: [string, any]) => (
                                <div key={key} className="bg-white dark:bg-gray-800 rounded-lg p-3 border border-yellow-200 dark:border-yellow-800">
                                    <div className="font-medium text-gray-700 dark:text-gray-300 text-sm mb-1">
                                        {interactionLabels[key] || key}
                                    </div>
                                    <div className={`text-xs font-medium ${getInteractionColor(value)}`}>
                                        {value}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {/* Warnings */}
                {payload.warnings && payload.warnings.length > 0 && (
                    <div className="bg-red-50 dark:bg-red-950/20 border border-red-200 dark:border-red-900 rounded-xl p-4">
                        <h3 className="font-semibold text-red-800 dark:text-red-300 mb-3 flex items-center gap-2">
                            🚨 {t('analyzer.result.warnings')}
                        </h3>
                        <ul className="space-y-2">
                            {payload.warnings.map((warning: string, i: number) => (
                                <li key={i} className="text-sm text-red-700 dark:text-red-400 flex items-start gap-2">
                                    <span className="text-red-500 mt-1">•</span>
                                    <span>{warning}</span>
                                </li>
                            ))}
                        </ul>
                    </div>
                )}

                {/* Notable Ingredients */}
                {payload.notable_ingredients && payload.notable_ingredients.length > 0 && (
                    <div>
                        <h3 className="text-sm font-medium text-gray-500 dark:text-gray-400 mb-3 uppercase tracking-wide">
                            ⭐ {t('analyzer.result.notable')}
                        </h3>
                        <div className="flex flex-wrap gap-2">
                            {payload.notable_ingredients.map((ing: string, i: number) => (
                                <span
                                    key={i}
                                    className="px-3 py-1.5 bg-purple-50 dark:bg-purple-900/20 text-purple-700 dark:text-purple-400 rounded-lg text-sm"
                                >
                                    {ing}
                                </span>
                            ))}
                        </div>
                    </div>
                )}

                {/* Detailed Ingredients Table */}
                {payload.ingredients_analyzed && payload.ingredients_analyzed.length > 0 && (
                    <details className="group border border-gray-200 dark:border-gray-700 rounded-xl">
                        <summary className="cursor-pointer font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white p-4 flex items-center gap-2">
                            <svg className="w-4 h-4 transition-transform group-open:rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                            </svg>
                            📋 {t('analyzer.result.fullList')} ({payload.ingredients_analyzed.length} {t('analyzer.result.ingredients')})
                        </summary>
                        <div className="p-4 pt-0 overflow-x-auto">
                            <table className="w-full text-sm">
                                <thead>
                                    <tr className="border-b border-gray-200 dark:border-gray-700">
                                        <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">#</th>
                                        <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">{t('analyzer.result.ingredient')}</th>
                                        <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">{t('analyzer.result.function')}</th>
                                        <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">{t('analyzer.result.safety')}</th>
                                        <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">{t('analyzer.result.comedogenic')}</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-100 dark:divide-gray-800">
                                    {payload.ingredients_analyzed.map((ing: any, i: number) => (
                                        <tr key={i} className="hover:bg-gray-50 dark:hover:bg-gray-800/50">
                                            <td className="px-3 py-2 text-gray-400">{i + 1}</td>
                                            <td className="px-3 py-2">
                                                <span className="font-medium text-gray-900 dark:text-white">{ing.name}</span>
                                                {ing.uncertain && (
                                                    <span className="ml-2 text-xs text-orange-600 dark:text-orange-400 bg-orange-100 dark:bg-orange-900/30 px-1.5 py-0.5 rounded">?</span>
                                                )}
                                            </td>
                                            <td className="px-3 py-2 text-gray-600 dark:text-gray-400 max-w-xs">
                                                {ing.function_vi || ing.function || '—'}
                                            </td>
                                            <td className="px-3 py-2">
                                                <span className={`px-2 py-0.5 rounded text-xs ${getSafetyStyle(ing.safety_level)}`}>
                                                    {ing.safety_level || '—'}
                                                </span>
                                            </td>
                                            <td className="px-3 py-2">
                                                <span className={`px-2 py-0.5 rounded text-xs ${getComedogenicStyle(ing.comedogenic_rating ?? 0)}`}>
                                                    {ing.comedogenic_rating ?? '—'}/5
                                                    {ing.comedogenic_warning && <span className="ml-1">⚠️</span>}
                                                </span>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </details>
                )}
            </div>
        </div>
    );
}
