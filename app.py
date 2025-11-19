from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Loic Buteau's Portfolio Data
PROFILE = {
    'name': 'Loic Buteau',
    'title': 'Quantitative Analyst & Financial Engineer',
    'bio': 'Financial engineer specializing in quantitative trading strategies, portfolio optimization, and statistical modeling. Passionate about leveraging Python and machine learning to solve complex financial problems.',
    'email': 'lmb2327@columbia.edu',
    'linkedin': 'https://linkedin.com/in/loicbuteau',
}

RESUME = {
    'experience': [
        {
            'title': 'Quantitative Analyst',
            'company': 'QED Trading',
            'period': 'Sep 2025 - Current',
            'description': 'Coded backtesting infrastructure for long-short algorithmic trading strategies, testing performance on 100+ market scenarios. Implemented framework to compute performance metrics (Sharpe Ratio, Sortino Ratio, Max Drawdown). Optimized strategy performance using grid search across parameter combinations.'
        },
        {
            'title': 'Senior Analyst - Investment Strategy Group',
            'company': 'ICONIQ Capital',
            'period': 'Feb 2025 - Jul 2025',
            'description': 'Audited and debugged portfolio allocation platform codebase in real time. Performed statistical modeling and forecasting of asset returns, volatility, and factor betas using regression analysis. Designed scenario analysis and stress test models to assess portfolio vulnerabilities.'
        },
        {
            'title': 'Sales and Trading Analytics Intern',
            'company': 'R.J. O\'Brien & Associates LLC',
            'period': 'Jun 2024 - Aug 2024',
            'description': 'Combined machine learning algorithms (OLS, ARIMA) to enhance revenue forecasting, reducing prediction error by 14%. Optimized capital allocation for 200 assets using integer programming to identify efficient frontier.'
        },
        {
            'title': 'Sales and Trading Intern (Fixed Income Desk)',
            'company': 'National Bank of Canada',
            'period': 'May 2023 - Aug 2023',
            'description': 'Applied PCA and clustering algorithms to analyze 80,000+ transactions from SQL database, uncovering key factors in bond pricing. Coded front-end applications for trading teams delivering quick relative value, yield, and DV01 insights.'
        },
        {
            'title': 'Trading Analyst Intern',
            'company': 'Pointus Partners',
            'period': 'May 2022 - Aug 2022',
            'description': 'Enhanced and backtested algorithmic pair-trading strategy using 5 years of market data. Developed trading signals from tick-level data leveraging market microstructure insights. Improved strategy with Hidden Markov Model to identify momentum regimes.'
        }
    ],
    'education': [
        {
            'degree': 'MS in Financial Engineering',
            'school': 'Columbia University',
            'year': '2024',
            'gpa': '3.8/4.0',
            'courses': 'Optimization, Stochastic Models, Monte Carlo Simulation, Machine Learning, Implied Volatility Smile, Term Structure'
        },
        {
            'degree': 'BBA in Finance - Quantitative Finance',
            'school': 'HEC Montreal',
            'year': '2023',
            'gpa': '4.24/4.30',
            'courses': 'Stochastic Models, Options and Futures, Portfolio Management, Quantitative Models in Finance'
        }
    ],
    'skills': ['Python', 'Pandas', 'NumPy', 'Matplotlib', 'CVXPY', 'SciPy', 'Plotly', 'Dash', 'Machine Learning', 'SQL', 'Bloomberg', 'Excel', 'VBA', 'GitHub', 'Claude Code']
}

PROJECTS = [
    {
        'title': 'Algorithmic Trading Backtesting Framework',
        'description': 'Built comprehensive backtesting infrastructure for long-short trading strategies, evaluating performance across 100+ market scenarios with advanced metrics including Sharpe Ratio, Sortino Ratio, and Max Drawdown.',
        'technologies': ['Python', 'Pandas', 'NumPy', 'Matplotlib'],
        'github': 'https://github.com/loicbuteau',
        'demo': None,
        'image': 'trading.jpg'
    },
    {
        'title': 'Portfolio Optimization Platform',
        'description': 'Statistical modeling and forecasting system for multi-asset portfolios using regression analysis, scenario testing, and stress analysis to assess portfolio vulnerabilities and optimize allocations.',
        'technologies': ['Python', 'CVXPY', 'SciPy', 'Pandas', 'Plotly'],
        'github': 'https://github.com/loicbuteau',
        'demo': None,
        'image': 'portfolio.jpg'
    },
    {
        'title': 'Double No-Touch Option Pricing',
        'description': 'Monte Carlo simulation framework for pricing exotic options under Black-Scholes, stochastic, and local volatility models. Academic project at Columbia University.',
        'technologies': ['Python', 'NumPy', 'Monte Carlo', 'Stochastic Calculus'],
        'github': 'https://github.com/loicbuteau',
        'demo': None,
        'image': 'options.jpg'
    },
    {
        'title': 'Bond Pricing Analysis Tool',
        'description': 'Applied PCA and clustering to analyze 80,000+ bond transactions, developing interpolation methods for real-time bond pricing and DV01 calculations for trading desk.',
        'technologies': ['Python', 'SQL', 'Pandas', 'Scikit-learn'],
        'github': 'https://github.com/loicbuteau',
        'demo': None,
        'image': 'bonds.jpg'
    },
    {
        'title': 'Pair Trading Strategy with HMM',
        'description': 'Enhanced algorithmic pair-trading strategy using Hidden Markov Models to identify momentum regimes, developing trading signals from tick-level market microstructure data.',
        'technologies': ['Python', 'Machine Learning', 'HMM', 'Market Data'],
        'github': 'https://github.com/loicbuteau',
        'demo': None,
        'image': 'pairs.jpg'
    },
    {
        'title': 'Revenue Forecasting Model',
        'description': 'Combined machine learning algorithms (OLS, ARIMA) to enhance revenue forecasting, reducing prediction error by 14% and improving model interpretability for capital allocation decisions.',
        'technologies': ['Python', 'Scikit-learn', 'ARIMA', 'Time Series'],
        'github': 'https://github.com/loicbuteau',
        'demo': None,
        'image': 'forecasting.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', profile=PROFILE)

@app.route('/resume')
def resume():
    return render_template('resume.html', profile=PROFILE, resume=RESUME)

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=PROFILE, projects=PROJECTS)

@app.route('/contact')
def contact():
    return render_template('contact.html', profile=PROFILE)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)