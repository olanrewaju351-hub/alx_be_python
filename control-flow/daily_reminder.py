# daily_reminder.py

priority = input("Enter the priority (high, medium, low): ")

if priority == "high":
    print("This is a high priority task! Handle it immediately.")
elif priority == "medium":
    print("This is a medium priority task. Plan to do it soon.")
elif priority == "low":
    print("This is a low priority task. You can do it later.")
else:
    print("Invalid priority entered.")

