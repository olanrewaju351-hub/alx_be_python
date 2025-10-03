# pattern_drawing.py
# Draw a square pattern of '*' of a user-specified size
# Outer loop uses while, inner loop uses for (as required).

size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")   # print '*' without newline
        print()                  # newline after finishing a row
        row += 1

