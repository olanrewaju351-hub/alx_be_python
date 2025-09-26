# temp_conversion_tool.py

# Global conversion factors (module-level globals)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    # We read the global FAHRENHEIT_TO_CELSIUS_FACTOR here
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    # We read the global CELSIUS_TO_FAHRENHEIT_FACTOR here
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def parse_temperature(value_str):
    """
    Try to convert the input string to float.
    If conversion fails, raise the required ValueError.
    """
    try:
        return float(value_str)
    except ValueError:
        # Requirement: raise this exact error message if invalid
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    try:
        temp_input = input("Enter the temperature value: ").strip()
        temp = parse_temperature(temp_input)   # may raise ValueError

        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()
        if unit in ("c", "celsius"):
            converted = convert_to_fahrenheit(temp)
            # print with two decimal places for readability
            print("Converted temperature: {:.2f} °F".format(converted))
        elif unit in ("f", "fahrenheit"):
            converted = convert_to_celsius(temp)
            print("Converted temperature: {:.2f} °C".format(converted))
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as err:
        # Show the raised error message to the user
        print(err)

if __name__ == "__main__":
    main()

