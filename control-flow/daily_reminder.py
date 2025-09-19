# daily_reminder.py
# Ask the user for one task, its priority and whether it is time-bound.
# Uses match / case for priority and an if to adjust the reminder when time-bound.

# Read inputs (trim spaces and normalize case where helpful)
task = input("Enter the task description: ").strip()
priority = input("Enter the priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound (yes/no): ").strip().lower()

# Build base text depending on priority (requires Python 3.10+ for match/case)
match priority:
    case "high":
        base = f"High priority task: {task}"
    case "medium":
        base = f"Medium priority task: {task}"
    case "low":
        base = f"Low priority task: {task}"
    case _:
        base = f"Task (unspecified priority): {task}"

# Use an if to modify the reminder if the task is time-bound
if time_bound == "yes":
    # Must include the phrase exactly as requested
    reminder = f"{base} — that requires immediate attention today!"
else:
    reminder = f"{base} — not time-sensitive; you can schedule it when convenient."

# Output the customized reminder
print(reminder)

