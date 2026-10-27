MONTHS_PER_YEAR = 12
PERCENT = 100

while True:
    try:
        if 0 < (monthly_investment := float(input(
            "Enter a monthly investment amount: "
        ))) < float("inf"):
            break
        print("Error: investment must be a positive number")
    except ValueError:
        print("Error: investment must be a number")

while True:
    try:
        if 0 < (yearly_interest_rate := float(input(
            "Enter a yearly interest rate: "
        ))) < float("inf"):
            break
        print("Error: yearly interest rate must be a positive number")
    except ValueError:
        print("Error: yearly interest rate must be a number")

while True:
    try:
        if (investment_years := int(input("Enter how many years to invest: "))) > 0:
            break
        print("Error: investment period must be a positive number of years")
    except ValueError:
        print("Error: investment period must be a whole number of years")

monthly_interest_rate = yearly_interest_rate / PERCENT / MONTHS_PER_YEAR
investment_months = investment_years * MONTHS_PER_YEAR
balance = 0.0

for month in range(1, investment_months + 1):
    # Each month's deposit earns interest immediately, matching the sample.
    balance += monthly_investment
    balance += balance * monthly_interest_rate
    if balance == float("inf"):
        print("Error: the investment balance exceeds the supported numeric range.")
        break
    print(f"Month {month} revenue: {balance}")
if balance < float("inf"):
    print(
        f"After {investment_years} years, you will receive a total investment "
        f"revenue of {balance:,.2f} at a yearly rate of {yearly_interest_rate}"
    )
