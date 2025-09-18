# finance_calculator.py

# prompt the user for monthly income and expenses (assume valid numbers)
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# project annual savings with a 5% simple annual interest
annual_interest_rate = 0.05  # 5%
projected_savings = monthly_savings * 12 * (1 + annual_interest_rate)

# print results (formatted to 2 decimal places)
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Projected savings after one year (including 5% interest): {projected_savings:.2f}")
