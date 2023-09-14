import pandas as pd
import numpy as np
import yfinance as yf
import datetime

# Define the NASDAQ tech stock or ETF symbol
symbol = "QQQ"  # Example: Invesco QQQ ETF

# Define the moving average window lengths
short_window = 50
long_window = 200

# Set the start and end date for historical data
start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2021, 12, 31)

# Download historical stock data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Calculate short-term and long-term moving averages
data['Short_MA'] = data['Adj Close'].rolling(window=short_window).mean()
data['Long_MA'] = data['Adj Close'].rolling(window=long_window).mean()

# Initialize trading signals
data['Signal'] = 0  # 1 for buy, -1 for sell

# Create a trading strategy based on moving average crossovers
for i in range(long_window, len(data)):
    if data['Short_MA'][i] > data['Long_MA'][i] and data['Short_MA'][i - 1] <= data['Long_MA'][i - 1]:
        data['Signal'][i] = 1  # Buy signal
    elif data['Short_MA'][i] < data['Long_MA'][i] and data['Short_MA'][i - 1] >= data['Long_MA'][i - 1]:
        data['Signal'][i] = -1  # Sell signal

# Calculate daily returns based on trading signals
data['Daily_Return'] = data['Adj Close'].pct_change() * data['Signal'].shift(1)

# Calculate cumulative returns
data['Cumulative_Return'] = (1 + data['Daily_Return']).cumprod()

# Print the performance metrics
print("Total Return:", data['Cumulative_Return'][-1])
print("Annualized Return:", ((data['Cumulative_Return'][-1]) ** (252 / len(data))) - 1)
print("Sharpe Ratio:", np.mean(data['Daily_Return']) / np.std(data['Daily_Return']) * np.sqrt(252))

# Visualize the strategy
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Adj Close'], label=symbol)
plt.plot(data.index, data['Short_MA'], label=f'{short_window}-day MA')
plt.plot(data.index, data['Long_MA'], label=f'{long_window}-day MA')
plt.plot(data.index, data['Signal'] * data['Adj Close'].max(), 'o', markersize=8, label='Buy/Sell Signal', alpha=0.7)
plt.legend(loc='best')
plt.title(f'{symbol} Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
