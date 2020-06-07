"""
Write a function that uses binary search to find an element
in a passed in list.
Returns the element if found.
Returns False if element not found.
"""

def binary_search(items, value):
    low = 0
    high = len(items) - 1

    while low <= high:
        middle = (low + high) // 2

        if value == items[middle]:
            return items[middle]

        if value > items[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return False


my_list = ["a", "b", "c", "d", "e", "f", "g"] 

result = binary_search(my_list, "e")
print(result == "e")

result = binary_search(my_list, "z")
print(result == False)
