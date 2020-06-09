"""
Write a function that takes a list of items and a value and
uses linear search to find the "index" of the value given.
Return the index if item is found
Returns False if item not found.
"""

def find_value(items, value):
    for i in range(len(items)):
        if items[i] == value:
            return i

    return False


my_list = ["a", "b", "c", "d", "e"]
result = find_value(my_list, "c")
print(result == 2)  

result = find_value(my_list, "e")
print(result == 4)  

result = find_value(my_list, "z")
print(result == False)  

