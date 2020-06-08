"""
Write a function that checks if a string is a palindrome.
The function takes a string and outputs True if it's a palindrome
and False if it's not.
"""


def is_palindrome(string):
    # if a string is of length 0 or 1, it's a palindrome
    if len(string) <= 1:
        return True

    # otherwise, compare first and last characters
    if string[0] == string[-1]:
        # if they are equal, strip those characters and check if
        # remaining characters are a palidrome
        return is_palindrome(string[1:-1])

    return False



string1 = "Hello"
string2 = "aabcddcbaa"

print(is_palindrome(string1) == False)
print(is_palindrome(string2) == True)
