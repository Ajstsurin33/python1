# Prompt the user to enter their weight in kilograms and height in meters
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI using the formula: BMI = Weight / (Height^2)
Bmi = weight / (height ^ 2)

# Display the calculated BMI, formatted to 2 decimal places
print("Your BMI is: {:.2f}".format(Bmi))



