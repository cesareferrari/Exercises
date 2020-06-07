"""
Write a function that uses binary search to find an element
in a passed in list.
Returns the element if found.
Returns False if element not found.
"""

def binary_search(items, value):
    pass


my_list = ["a", "b", "c", "d", "e", "f", "g"] 

result = binary_search(my_list, "e")
print(result == "e")  # True

result = binary_search(my_list, "z")
print(result == False)   # True
