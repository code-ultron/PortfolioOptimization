# Stock Price Forecasting & Portfolio Optimization

This project combines advanced time series forecasting and portfolio optimization techniques to assist in stock investment decision-making. It leverages Long Short-Term Memory (LSTM) neural networks for predicting stock prices and utilizes Monte Carlo simulations for optimizing portfolio allocation.

## Key Features

### Stock Price Forecasting
- **LSTM-Based Prediction**: Uses LSTM neural networks, well-suited for capturing the temporal dependencies in time series data, to predict future stock prices.
- **Customizable Forecasting Period**: Allows users to predict stock prices for a specified number of future days, providing flexibility in time horizons.

The historical stock data with the newly predicted data is saved as combined_stock_data.csv and passed as input for the API.

### Portfolio Optimization via Monte Carlo Simulation
- **Monte Carlo Simulations**: Generates thousands of random portfolio combinations to simulate possible outcomes.
- **Risk and Return Metrics**: Calculates key portfolio metrics, including:
  - **Sharpe Ratio**: Measures the risk-adjusted return of the portfolio.
  - **Value at Risk (VaR)**: Estimates the potential loss in the portfolio's value at a specified confidence level.
  - **Conditional Value at Risk (CVaR)**: Evaluates the average loss beyond the VaR, providing a more conservative risk assessment.
- **Optimal Portfolio Identification**: Selects the optimal portfolio weights based on the highest Sharpe ratio, maximizing return for a given level of risk.


# Predicting future stock prices using LSTM enhances Monte Carlo portfolio optimization by incorporating anticipated market trends into expected returns and volatility calculations. This forward-looking approach results in more accurate simulations, aligning portfolio allocation with potential future market conditions for optimized returns and risk management.

## Project Structure

- `portfolio_optimization.py`: Contains the code for running the Monte Carlo simulation and finding the optimal portfolio based on historical stock price data.
- `lstm_forecasting.ipynb`: Implements the LSTM model for forecasting stock prices.
- `app.py`: A Flask-based API that allows users to upload a stock data CSV file, run the optimization process, and return the optimal portfolio allocation and metrics.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `request.py`: The sample request to the API

### Prerequisites
- Python 3.8 or higher
- Required libraries (install using `pip`):
  ```bash
  pip install -r requirements.txt

## How to Use

1. First run the python app.py to run the Flask App
2. 
3. Open the second terminal and run python request.py to send the POST request to API hosted on the local

## Results

- `result/optimization_result.txt`: 

This output includes the annualized return, annualized volatility, and Sharpe ratio for the optimized portfolio, as well as the dollar allocation and optimal weights for each stock. These metrics help investors make data-driven decisions by understanding the risk-adjusted performance of the selected portfolio.
