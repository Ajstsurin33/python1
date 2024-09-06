#
#
#

#Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
#If the current number is even, divide it by 2.
#If the current number is odd, multiply it by 3 and add 1.

user_input = input("Enter a Pos interger: ")
while True:
    if user_input():
        number = int(user_input)
        if number > 0:
            break
        else:
            user_input = input("The Number must be a postive int, Enter again: ")
        else:
        user_input = input("invalid Input. Please Enter Pos int: " )
        print('collatz Squance: ')

        while number != 1:
        print(number,->'')
        if number = number // 2
        else:
            number = 3 * number + 1

            print(1)