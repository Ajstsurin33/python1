####

##
#
def calculate_grade(average):

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
        while True:
            try:
                marks1 = float(input("Enter marks for subject 1: "))
                marks2 = float(input("Enter marks for subject 2: "))
                marks3 = float(input("Enter marks for subject 3: "))
                break
            except ValueError:
             print("Invalid input. Please enter numeric values for the marks.")


average = ( marks1 + marks2 + marks3 ) / 3
grade = calculate_grade(average)
print(f"Your average mark is: {average:.2f}")
print(f"Your grade is: {grade}")


