import React from 'react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

export default function About() {
    const { t } = useTranslation();

    const techStack = [
        { name: 'React', icon: '⚛️', desc: 'Frontend Framework' },
        { name: 'TypeScript', icon: '📘', desc: 'Type Safety' },
        { name: 'Tailwind CSS', icon: '🎨', desc: 'Styling' },
        { name: 'Vite', icon: '⚡', desc: 'Build Tool' },
        { name: 'Express.js', icon: '🖥️', desc: 'Backend Server' },
        { name: 'Gemini AI', icon: '🤖', desc: 'AI Analysis' },
    ];

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-50 via-blue-50 to-pink-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-12 px-4">
            <div className="max-w-5xl mx-auto">
                {/* Header */}
                <header className="text-center mb-16">
                    <div className="inline-block mb-4">
                        <span className="text-6xl">ℹ️</span>
                    </div>
                    <h1 className="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-purple-600 via-blue-600 to-pink-600 bg-clip-text text-transparent mb-3">
                        {t('about.title')}
                    </h1>
                    <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
                        {t('about.subtitle')}
                    </p>
                </header>

                {/* Mission Section */}
                <section className="mb-12">
                    <div className="bg-gradient-to-r from-purple-500 to-pink-500 rounded-3xl p-8 md:p-12 text-white shadow-2xl">
                        <div className="flex flex-col md:flex-row items-center gap-8">
                            <div className="flex-shrink-0">
                                <div className="w-24 h-24 bg-white/20 rounded-full flex items-center justify-center">
                                    <span className="text-5xl">🎯</span>
                                </div>
                            </div>
                            <div>
                                <h2 className="text-2xl md:text-3xl font-bold mb-4">{t('about.mission.title')}</h2>
                                <p className="text-white/90 text-lg leading-relaxed">
                                    {t('about.mission.desc')}
                                </p>
                            </div>
                        </div>
                    </div>
                </section>

                {/* Technology Section */}
                <section className="mb-12">
                    <div className="bg-white dark:bg-gray-800 rounded-3xl p-8 shadow-xl border border-gray-200 dark:border-gray-700">
                        <div className="flex items-center gap-3 mb-8">
                            <span className="text-3xl">🛠️</span>
                            <h2 className="text-2xl font-bold text-gray-800 dark:text-white">{t('about.tech.title')}</h2>
                        </div>

                        <p className="text-gray-600 dark:text-gray-400 mb-8">
                            {t('about.tech.desc')}
                        </p>

                        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                            {techStack.map((tech, index) => (
                                <div
                                    key={index}
                                    className="bg-gray-50 dark:bg-gray-700/50 rounded-xl p-4 text-center hover:shadow-lg hover:-translate-y-1 transition-all duration-300"
                                >
                                    <div className="text-3xl mb-2">{tech.icon}</div>
                                    <h3 className="font-semibold text-gray-800 dark:text-white">{tech.name}</h3>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">{tech.desc}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* How It Works */}
                <section className="mb-12">
                    <div className="bg-white dark:bg-gray-800 rounded-3xl p-8 shadow-xl border border-gray-200 dark:border-gray-700">
                        <div className="flex items-center gap-3 mb-8">
                            <span className="text-3xl">⚙️</span>
                            <h2 className="text-2xl font-bold text-gray-800 dark:text-white">
                                {t('home.howItWorks.title')}
                            </h2>
                        </div>

                        <div className="relative">
                            {/* Timeline */}
                            <div className="absolute left-6 top-0 bottom-0 w-0.5 bg-gradient-to-b from-purple-500 to-pink-500 hidden md:block"></div>

                            <div className="space-y-8">
                                <div className="flex gap-6 items-start">
                                    <div className="flex-shrink-0 w-12 h-12 bg-purple-500 rounded-full flex items-center justify-center text-white font-bold shadow-lg">
                                        1
                                    </div>
                                    <div>
                                        <h3 className="font-semibold text-gray-800 dark:text-white mb-2">Upload Image</h3>
                                        <p className="text-gray-600 dark:text-gray-400">
                                            User uploads or captures a photo of the cosmetic product's ingredient list.
                                        </p>
                                    </div>
                                </div>

                                <div className="flex gap-6 items-start">
                                    <div className="flex-shrink-0 w-12 h-12 bg-pink-500 rounded-full flex items-center justify-center text-white font-bold shadow-lg">
                                        2
                                    </div>
                                    <div>
                                        <h3 className="font-semibold text-gray-800 dark:text-white mb-2">AI Processing</h3>
                                        <p className="text-gray-600 dark:text-gray-400">
                                            Google Gemini AI extracts and analyzes each ingredient using advanced vision capabilities.
                                        </p>
                                    </div>
                                </div>

                                <div className="flex gap-6 items-start">
                                    <div className="flex-shrink-0 w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold shadow-lg">
                                        3
                                    </div>
                                    <div>
                                        <h3 className="font-semibold text-gray-800 dark:text-white mb-2">Detailed Report</h3>
                                        <p className="text-gray-600 dark:text-gray-400">
                                            Receive a comprehensive analysis including safety ratings, comedogenic scores, and recommendations.
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                {/* Disclaimer */}
                <section className="mb-12">
                    <div className="bg-amber-50 dark:bg-amber-900/20 rounded-3xl p-8 border-2 border-amber-200 dark:border-amber-800">
                        <div className="flex items-start gap-4">
                            <div className="flex-shrink-0">
                                <span className="text-4xl">⚠️</span>
                            </div>
                            <div>
                                <h2 className="text-xl font-bold text-amber-800 dark:text-amber-300 mb-3">
                                    {t('about.disclaimer.title')}
                                </h2>
                                <p className="text-amber-700 dark:text-amber-400 leading-relaxed">
                                    {t('about.disclaimer.desc')}
                                </p>
                            </div>
                        </div>
                    </div>
                </section>

                {/* CTA */}
                <section className="text-center">
                    <div className="bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 rounded-3xl p-8 md:p-12 text-white shadow-2xl">
                        <h2 className="text-2xl md:text-3xl font-bold mb-4">
                            {t('home.cta.title')}
                        </h2>
                        <p className="text-white/80 mb-8">
                            {t('home.cta.subtitle')}
                        </p>
                        <Link
                            to="/analyze"
                            className="inline-flex items-center gap-2 bg-white text-purple-600 px-8 py-4 rounded-full font-bold text-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
                        >
                            <span>{t('common.getStarted')}</span>
                            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                            </svg>
                        </Link>
                    </div>
                </section>
            </div>
        </div>
    );
}
