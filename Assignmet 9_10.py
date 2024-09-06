#
#
#
#

def is_vowel(char):
    vowels = 'aeiou'
    return char.lower() in vowels

def main():
    # Prompt the user to enter a single character
    while True:
        char = input("Enter a single character: ")
        if len(char) == 1 and char.isalpha():
            break
        else:
            print("Invalid input. Please enter exactly one alphabetical character.")

    # Determine if the character is a vowel or consonant
    if is_vowel(char):
        print(f"The character '{char}' is a vowel.")
    else:
        print(f"The character '{char}' is a consonant.")

if __name__ == "__main__":
    main()


#__________________________________________________________________________________________________________________________________________________________________________________________



def classify_age(age):

    if age < 18:
        return 'Minor'
    elif 18 <= age <= 65:
        return 'Adult'
    else:
        return 'Senior citizen'

def main():
    # Prompt them to enter their age
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")

    # Determine age category
    category = classify_age(age)
g
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
