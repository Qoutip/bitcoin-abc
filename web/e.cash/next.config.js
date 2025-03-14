// Copyright (c) 2023 The Bitcoin developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.
const nextConfig = {
    reactStrictMode: true,
    compiler: {
        styledComponents: true,
    },
    eslint: {
        dirs: [
            'pages',
            'app',
            'components',
            'lib',
            'src',
            'data',
            'styles',
            '.eslintrc.js',
            'next.config.js',
            'jest.config.js',
        ],
    },
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'api.scorecard.cash',
            },
        ],
    },
};

module.exports = nextConfig;
