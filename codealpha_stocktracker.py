def stock_tracker():
    # Hardcoded prices as per instructions
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 175
    }

    portfolio = {}
    print("--- Stock Portfolio Tracker ---")
    
    # User input
    for stock in stock_prices:
        shares = int(input(f"How many shares of {stock} do you own? "))
        portfolio[stock] = shares

    # Calculation
    total_value = 0
    print("\n--- Portfolio Summary ---")
    for stock, shares in portfolio.items():
        value = shares * stock_prices[stock]
        total_value += value
        print(f"{stock}: {shares} shares | Value: ${value}")
	print("-" * 25)
    print(f"Total Investment Value: ${total_value}")

stock_tracker()