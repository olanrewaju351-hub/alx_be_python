# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.

    Parameters:
      - num1 (float)
      - num2 (float)
      - operation (str): one of 'add', 'subtract', 'multiply', 'divide'

    Returns:
      - float result for valid operations
      - string error message for division by zero or invalid operation
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

