"""
Implement the Quicksort algorithm to sort a list of numbers in ascending order
using recursion.
The function doesn't modify the original list, but returns a new sorted list.

Algorithm:
1. choose a pivot
2. move everything less than the pivot to one side
3. move everything more than the pivot to the other side
4. repeat steps 1 to 3 on the left hand side and right hand side of the partition
"""

def partition(items):
    left = []
    right = []
    pivot = items[0]

    # iterate over the rest of the array
    for item in items[1:]:
        # if item > pivot, append to right
        if item > pivot:
            right.append(item)
        # else append to left
        else:
            left.append(item)

    # return tuple
    return left, pivot, right

def quicksort(items):
    if len(items) <= 1:
        return items

    # assign returned tuple values to local variables
    left, pivot, right = partition(items)

    return quicksort(left) + [pivot] + quicksort(right)


items = [3, 6, 1, 5, 3, 4, 2]
print(quicksort(items) == [1, 2, 3, 3, 4, 5, 6])  # --> True
print(items == [3, 6, 1, 5, 3, 4, 2])             # --> True

