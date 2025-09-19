# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

# Use match-case (Python 3.10+) for priority handling
match priority:
    case "high":
        print(f"The result is: '{task}' is a HIGH priority task! Handle it immediately.")
    case "medium":
        print(f"The result is: '{task}' is a MEDIUM priority task. Plan to do it soon.")
    case "low":
        print(f"The result is: '{task}' is a LOW priority task. You can do it later.")
    case _:
        print("Invalid priority entered.")

