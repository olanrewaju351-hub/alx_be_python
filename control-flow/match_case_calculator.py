# match_case_calculator.py
# Simple calculator that uses a Python 3.10+ match / case statement.

def get_number(prompt):
    """Prompt repeatedly until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number (e.g. 3.5 or 10).")

# 1) Read user input (num1, num2, operation)
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ").strip()

# 2) Use match / case to perform the chosen operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Unknown operation. Please choose one of +, -, *, /.")

