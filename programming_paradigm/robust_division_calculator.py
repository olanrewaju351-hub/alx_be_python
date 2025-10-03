# robust_division_calculator.py

def robust_division_calculator():
    """A simple calculator that divides two numbers with error handling."""
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        result = num1 / num2
        print(f"The result is {result}")

    except ZeroDivisionError:
        # EXACT string required
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    robust_division_calculator()

