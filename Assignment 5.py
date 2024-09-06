def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompt the user to enter a time duration in hours
hours = get_numeric_input("Enter a time duration in hours: ")

# Convert the time duration to minutes and seconds
total_minutes = hours * 60
total_seconds = hours * 3600

# Calculate minutes and seconds from total seconds
minutes = int(total_minutes)
seconds = int(total_seconds % 60)

# Display the converted time duration in minutes and seconds
print(f"The time duration is: {minutes} minutes and {seconds} seconds.")
