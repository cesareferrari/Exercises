"""
Write a function that takes a string and outputs the string reversed.
Use recursion (call the function inside the function).
"""

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


string = "Hello, World!"
result = reverse_string(string)
print(result == "!dlroW ,olleH")
