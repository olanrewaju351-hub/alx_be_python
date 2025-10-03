# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.
    - Accepts numbers or numeric strings.
    - Returns a float result on success.
    - Returns a string error message on failure.
    """
    # Try converting inputs to floats (handle non-numeric input)
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        return "Error: Non-numeric input. Please enter valid numbers."

    # Try performing the division (handle division by zero)
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    return result
