def merge(left, right):
    merged = []

    # initialize the pointers that start at each array
    a = 0
    b = 0

    while a < len(left) and b < len(right):
        # compare the elements where a and b point to
        # and append the correct element from left or right array to merged
        if left[a] < right[b]:
            merged.append(left[a])
            a += 1
        else:
            merged.append(right[b])
            b += 1

    # Now one list is empty, append the rest of the elements
    # from the other list to merged.
    # Only one of these loops is going to run
    while a < len(left):
        merged.append(left[a])
        a += 1

    while b < len(right):
        merged.append(right[b])
        b += 1

    return merged


def merge_sort(arr):
    # base case: when list is length of 1
    if len(arr) <= 1:
        return arr

    # if length more than 1, set a splitting point and
    # break the array down into 2 subarrays recursively
    split = len(arr) // 2
    
    # left half contains elements from 0 to splitting point
    left = merge_sort(arr[:split])
    # right half contains elements from splitting to end
    right = merge_sort(arr[split:])

    # merge them back up
    return merge(left, right)





