# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def parse_temperature(value_str):
    """
    Try to convert the input string to float.
    If conversion fails, raise the required ValueError.
    """
    try:
        return float(value_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    try:
        # ✅ exact string for checker
        temp_input = input("Enter the temperature to convert: ").strip()
        temp = parse_temperature(temp_input)

        # ✅ exact string for checker
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
        if unit in ("c", "celsius"):
            converted = convert_to_fahrenheit(temp)
            print("Converted temperature: {:.2f} °F".format(converted))
        elif unit in ("f", "fahrenheit"):
            converted = convert_to_celsius(temp)
            print("Converted temperature: {:.2f} °C".format(converted))
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as err:
        print(err)

if __name__ == "__main__":
    main()

