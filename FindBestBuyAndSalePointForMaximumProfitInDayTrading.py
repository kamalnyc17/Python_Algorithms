# find the maximum profit of a trade from following stock price
stock_prices = [70, 20, 15, 10, 7, 19, 8, 11, 30, 9, 85, 1, 21, 9, 37, 100]


def get_max_profit(stock_prices):
    max_profit = 0
    for i in range(len(stock_prices)):
        buy_price = stock_prices[i]
        for j in range(i+1, len(stock_prices)):
            sale_price = stock_prices[j]
            potential_profit = sale_price - buy_price
            # storing current maximum profit if it's greater than previous max value
            max_profit = max(max_profit, potential_profit)
    return max_profit


# calling the function
print(f"Maximum Profit: {get_max_profit(stock_prices)}")
