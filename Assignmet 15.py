#
#
#
def is_palindrome(s):

    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

string1 = "A man, a plan, a canal, Panama"
string2 = "Hello, World!"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
