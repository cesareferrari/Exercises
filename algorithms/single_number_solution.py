'''
Given a non-empty array of integers where every element appears twice except for
one. Find that single number. You may assume that there will always be one
odd-number-out and every other number in the input shows up exactly twice.

Examples

Sample input: [2, 2, 1]
Expected output: 1

Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
'''
def single_number(arr):

    singles = []

    for n in arr:
        if n in singles:
            singles.remove(n)
        else:
            singles.append(n)

    return singles[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
