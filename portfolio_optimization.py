import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_optimization(file_path, total_fund=1000):
    # Load the dataset
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

    # Ensure that the price columns are numeric
    columns_to_convert = ['open', 'high', 'low', 'close', 'volume']
    for col in columns_to_convert:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with NaN values that might result from conversion errors
    data.dropna(subset=columns_to_convert, inplace=True)

    # Pivot the data to get closing prices with 'context_id' as columns and 'date' as index
    pivot_data = data.pivot_table(values='close', index='date', columns='context_id')

    # Calculate daily returns for each stock (each column represents a stock)
    returns = pivot_data.pct_change().dropna()

    # Define parameters for the Monte Carlo simulation
    num_portfolios = 100000
    np.random.seed(42)

    # Generate random portfolios and calculate metrics
    results = np.zeros((4, num_portfolios))
    weights_record = []

    for i in range(num_portfolios):
        weights = np.random.random(len(returns.columns))
        weights /= np.sum(weights)
        weights_record.append(weights)
        
        portfolio_return = np.sum(returns.mean() * weights) * 252  # Annualized return
        portfolio_stddev = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))  # Annualized volatility
        sharpe_ratio = portfolio_return / portfolio_stddev
        
        results[0, i] = portfolio_return
        results[1, i] = portfolio_stddev
        results[2, i] = sharpe_ratio
        results[3, i] = np.sum(weights > 0)

    # Identify the portfolio with the maximum Sharpe ratio
    max_sharpe_idx = np.argmax(results[2])
    optimal_weights = weights_record[max_sharpe_idx]
    optimal_portfolio_return = results[0, max_sharpe_idx]
    optimal_portfolio_stddev = results[1, max_sharpe_idx]
    optimal_sharpe_ratio = results[2, max_sharpe_idx]

    # Map stock names to their weights in the optimal portfolio
    stock_names = returns.columns
    optimal_weights_dict = dict(zip(stock_names, optimal_weights))

    # Calculate the allocation of the total budget based on the optimal weights
    dollar_allocation = {stock: weight * total_fund for stock, weight in optimal_weights_dict.items()}

    # Prepare results
    results_dict = {
        "optimal_weights": optimal_weights_dict,
        "annualized_return": optimal_portfolio_return,
        "annualized_volatility": optimal_portfolio_stddev,
        "sharpe_ratio": optimal_sharpe_ratio,
        "dollar_allocation": dollar_allocation
    }

    return results_dict
