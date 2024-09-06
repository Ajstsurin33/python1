#
#
#
#Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.
def right_triangle(rows):

    for i in range(1, rows + 1):
        print('*' * i)


def main():

    while True:
        try:
            num_rows = int(input("Enter the number of rows for the patern: "))
            if num_rows <= 0:
                raise ValueError("The number of rows must be a positve integer.")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid positve integer.")

    right_triangle(num_rows)


if __name__ == "__main__":
    main()

