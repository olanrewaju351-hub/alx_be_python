# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: obtain and display the current date and time.
    Saves the datetime in 'current_date' and prints in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.now()  # save current date/time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # returning it is helpful if caller wants to reuse it

def calculate_future_date():
    """
    Part 2: prompt user for a number of days, compute the future date,
    save it in 'future_date' and print as "YYYY-MM-DD".
    """
    # prompt exactly as required
    days_str = input("Enter the number of days to add to the current date: ").strip()
    try:
        days = int(days_str)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

    # Use current date/time as base
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # save future_date variable
    print(f"Future date after {days} day(s): {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # Part 1
    display_current_datetime()

    # Part 2
    calculate_future_date()

if __name__ == "__main__":
    main()

