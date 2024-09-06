def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. enter a numeric value.")

# (e.g., 1 USD = 0.85 EUR)
exchange_rate = 0.85

# source currency (e.g., USD)
amount_usd = get_numeric_input("Enter the amount in USD: ")

# Convert  target currency
amount_eur = amount_usd * exchange_rate

# Display amount
print(f"The amount in EUR is: {amount_eur:}")
