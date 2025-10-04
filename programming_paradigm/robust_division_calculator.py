def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / den
        return f"Result: {result}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."


