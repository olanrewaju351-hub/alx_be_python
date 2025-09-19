# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

# Check if task is time-bound
if time_bound == "yes":
    print(f"Reminder: '{task}' is time-bound. Handle it on schedule!")
else:
    print(f"Reminder: '{task}' is not time-bound. You can plan accordingly.")

# Handle priority using match-case (Python 3.10+)
match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task! Handle it immediately.")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task. Plan to do it soon.")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task. You can do it later.")
    case _:
        print("Reminder: Invalid priority entered.")

