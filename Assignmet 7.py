#
#
# Prompt the user to enter a year.

#Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.

#Output: Display whether the entered year is a leap year or not.

def leap_year(year):

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():

    while True:
        try:
            year = int(input("enter a year: "))
            break
        except ValueError:
            print("Invalid input. please enter a valid year.")


    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
