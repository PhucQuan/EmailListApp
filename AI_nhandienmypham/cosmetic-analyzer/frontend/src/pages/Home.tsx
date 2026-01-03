import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

export default function Home() {
    const { t } = useTranslation();

    const stats = [
        { value: '10,000+', labelKey: 'homePage.stats.ingredients' },
        { value: '50+', labelKey: 'homePage.stats.brands' },
        { value: '99%', labelKey: 'homePage.stats.accuracy' },
    ];

    const features = [
        {
            icon: (
                <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
            ),
            titleKey: 'homePage.features.smart.title',
            descKey: 'homePage.features.smart.desc',
        },
        {
            icon: (
                <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
            ),
            titleKey: 'homePage.features.safety.title',
            descKey: 'homePage.features.safety.desc',
        },
        {
            icon: (
                <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
            ),
            titleKey: 'homePage.features.instant.title',
            descKey: 'homePage.features.instant.desc',
        },
        {
            icon: (
                <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
            ),
            titleKey: 'homePage.features.chat.title',
            descKey: 'homePage.features.chat.desc',
        },
    ];

    const steps = [
        { num: '01', titleKey: 'homePage.steps.step1.title', descKey: 'homePage.steps.step1.desc' },
        { num: '02', titleKey: 'homePage.steps.step2.title', descKey: 'homePage.steps.step2.desc' },
        { num: '03', titleKey: 'homePage.steps.step3.title', descKey: 'homePage.steps.step3.desc' },
    ];

    const testimonials = [
        {
            quoteKey: 'homePage.testimonials.t1.quote',
            author: "Minh Anh",
            roleKey: 'homePage.testimonials.t1.role',
        },
        {
            quoteKey: 'homePage.testimonials.t2.quote',
            author: "Thu Hương",
            roleKey: 'homePage.testimonials.t2.role',
        },
        {
            quoteKey: 'homePage.testimonials.t3.quote',
            author: "Quốc Bảo",
            roleKey: 'homePage.testimonials.t3.role',
        },
    ];

    return (
        <div className="bg-white dark:bg-gray-950">
            {/* Hero Section - Clean & Minimal */}
            <section className="relative overflow-hidden">
                {/* Subtle background pattern */}
                <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgba(236,72,153,0.05),transparent_50%)] dark:bg-[radial-gradient(circle_at_30%_20%,rgba(236,72,153,0.1),transparent_50%)]"></div>

                <div className="relative max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-24 lg:pt-32 lg:pb-32">
                    <div className="text-center max-w-3xl mx-auto">
                        {/* Headline */}
                        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
                            {t('homePage.hero.title1')}{' '}
                            <span className="text-pink-600 dark:text-pink-400">{t('homePage.hero.highlight')}</span>
                            {' '}{t('homePage.hero.title2')}
                        </h1>

                        {/* Subheadline */}
                        <p className="text-lg sm:text-xl text-gray-600 dark:text-gray-400 mb-10 leading-relaxed">
                            {t('homePage.hero.subtitle')}
                        </p>

                        {/* CTA Buttons */}
                        <div className="flex flex-col sm:flex-row gap-4 justify-center">
                            <Link
                                to="/analyze"
                                className="inline-flex items-center justify-center gap-2 px-8 py-4 bg-gray-900 dark:bg-white text-white dark:text-gray-900 rounded-xl font-semibold hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors"
                            >
                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                                </svg>
                                {t('homePage.hero.cta')}
                            </Link>
                            <Link
                                to="/knowledge"
                                className="inline-flex items-center justify-center gap-2 px-8 py-4 border-2 border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-300 rounded-xl font-semibold hover:border-gray-300 dark:hover:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors"
                            >
                                {t('common.learnMore')}
                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                                </svg>
                            </Link>
                        </div>
                    </div>
                </div>
            </section>

            {/* Stats Section */}
            <section className="border-y border-gray-100 dark:border-gray-800 bg-gray-50/50 dark:bg-gray-900/50">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                    <div className="grid grid-cols-3 gap-8">
                        {stats.map((stat, i) => (
                            <div key={i} className="text-center">
                                <div className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-1">
                                    {stat.value}
                                </div>
                                <div className="text-sm text-gray-500 dark:text-gray-400">
                                    {t(stat.labelKey)}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="py-20 lg:py-28">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-16">
                        <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
                            {t('homePage.features.title')}
                        </h2>
                        <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
                            {t('homePage.features.subtitle')}
                        </p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {features.map((feature, i) => (
                            <div
                                key={i}
                                className="group p-6 rounded-2xl border border-gray-100 dark:border-gray-800 hover:border-pink-200 dark:hover:border-pink-800 hover:bg-pink-50/30 dark:hover:bg-pink-950/20 transition-all duration-300"
                            >
                                <div className="w-12 h-12 rounded-xl bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-600 dark:text-gray-400 group-hover:bg-pink-100 dark:group-hover:bg-pink-900/30 group-hover:text-pink-600 dark:group-hover:text-pink-400 transition-colors mb-4">
                                    {feature.icon}
                                </div>
                                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                                    {t(feature.titleKey)}
                                </h3>
                                <p className="text-gray-600 dark:text-gray-400 leading-relaxed">
                                    {t(feature.descKey)}
                                </p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* How It Works */}
            <section className="py-20 lg:py-28 bg-gray-50 dark:bg-gray-900">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-16">
                        <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
                            {t('homePage.howItWorks.title')}
                        </h2>
                        <p className="text-lg text-gray-600 dark:text-gray-400">
                            {t('homePage.howItWorks.subtitle')}
                        </p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                        {steps.map((step, i) => (
                            <div key={i} className="relative">
                                {i < steps.length - 1 && (
                                    <div className="hidden md:block absolute top-12 left-full w-full h-px bg-gray-200 dark:bg-gray-700 -translate-x-1/2"></div>
                                )}
                                <div className="text-center">
                                    <div className="inline-flex items-center justify-center w-24 h-24 rounded-full bg-white dark:bg-gray-800 shadow-sm border border-gray-100 dark:border-gray-700 mb-6">
                                        <span className="text-3xl font-bold text-pink-600 dark:text-pink-400">{step.num}</span>
                                    </div>
                                    <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                                        {t(step.titleKey)}
                                    </h3>
                                    <p className="text-gray-600 dark:text-gray-400">
                                        {t(step.descKey)}
                                    </p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Testimonials */}
            <section className="py-20 lg:py-28">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-16">
                        <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
                            {t('homePage.testimonials.title')}
                        </h2>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {testimonials.map((item, i) => (
                            <div
                                key={i}
                                className="p-6 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800"
                            >
                                <svg className="w-8 h-8 text-pink-300 dark:text-pink-700 mb-4" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z" />
                                </svg>
                                <p className="text-gray-700 dark:text-gray-300 mb-6 leading-relaxed">
                                    "{t(item.quoteKey)}"
                                </p>
                                <div>
                                    <div className="font-semibold text-gray-900 dark:text-white">{item.author}</div>
                                    <div className="text-sm text-gray-500 dark:text-gray-400">{t(item.roleKey)}</div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="py-20 lg:py-28 bg-gray-900 dark:bg-gray-950">
                <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                    <h2 className="text-3xl sm:text-4xl font-bold text-white mb-6">
                        {t('homePage.cta.title')}
                    </h2>
                    <p className="text-lg text-gray-400 mb-10 max-w-2xl mx-auto">
                        {t('homePage.cta.subtitle')}
                    </p>
                    <Link
                        to="/analyze"
                        className="inline-flex items-center justify-center gap-2 px-8 py-4 bg-white text-gray-900 rounded-xl font-semibold hover:bg-gray-100 transition-colors"
                    >
                        {t('homePage.cta.button')}
                        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                        </svg>
                    </Link>
                </div>
            </section>
        </div>
    );
}
