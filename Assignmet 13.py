#
#
#
#Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
def palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned_string == cleaned_string[:-1]

def main():

    user_input = input("Enter a string to check if it's a palindrome: ")
    if palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()
