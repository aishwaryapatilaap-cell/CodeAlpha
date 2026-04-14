# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

def calculate_investment():
    total_investment = 0
    portfolio = {}

    print("Available stocks:", list(stock_prices.keys()))
    
    n = int(input("Enter number of different stocks you want to invest in: "))

    for _ in range(n):
        stock = input("Enter stock name: ").upper()

        if stock not in stock_prices:
            print("Stock not available. Skipping...")
            continue

        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity

    print("\nYour Portfolio:")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment
        print(f"{stock}: {quantity} shares × {price} = {investment}")

    print("\nTotal Investment Value:", total_investment)

    # Save to file
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} × {price} = {investment}\n")
        file.write(f"\nTotal Investment: {total_investment}")

    print("\nPortfolio saved to 'portfolio.txt'")


# Run program
calculate_investment()
