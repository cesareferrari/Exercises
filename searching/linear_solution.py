"""
Write a function that takes a list of items and a value and
uses linear search to find the value given.
Returns False if item not found.
"""

def find_value(items, value):
    for item in items:
        if item == value:
            return item

    return False


my_list = ["a", "b", "c", "d", "e"]
result = find_value(my_list, "c")
print(result)   # -> c

result = find_value(my_list, "z")
print(result)   # -> False

