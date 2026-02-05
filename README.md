# Mortgage Calculator

A Streamlit application for calculating mortgage payments and analyzing loan scenarios.

## Features

- **Payment Calculation**: Compute monthly mortgage payments based on principal, interest rate, and loan term
- **Amortization Schedule**: View detailed payment breakdown over time
- **Scenario Comparison**: Compare different loan terms and interest rates
- **Visual Charts**: Interactive graphs showing payment trends and principal/interest breakdown

## Installation

```bash
pip install streamlit
```

## Usage

```bash
streamlit run app.py
```

## How It Works

This calculator uses the standard mortgage formula to determine monthly payments:
- M = P[r(1+r)^n]/[(1+r)^n-1]
- Where M = monthly payment, P = principal, r = monthly rate, n = number of payments

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- Plotly (for visualizations)

## License

MIT License