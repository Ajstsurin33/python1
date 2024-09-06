x = 5
y = 3

print(x * y)

import math

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompt the user to enter the coordinates of the first point (x1, y1)
x1 = get_numeric_input("Enter the x-coordinate of the first point: ")
y1 = get_numeric_input("Enter the y-coordinate of the first point: ")

# Prompt the user to enter the coordinates of the second point (x2, y2)
x2 = get_numeric_input("Enter the x-coordinate of the second point: ")
y2 = get_numeric_input("Enter the y-coordinate of the second point: ")

# Calculate the distance between the two points using the distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the calculated distance
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
