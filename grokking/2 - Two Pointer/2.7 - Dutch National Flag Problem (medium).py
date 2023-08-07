# Given an array containing 0s, 1s and 2s, sort the array in-place.
# Treat numbers as objects, not counting 0s, 1s, and 2s.
# This problem is known as the Dutch National Flag problem.
# The flag of the Netherlands has colors: red, white, blue.

# Example 1:
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]

# Example 2:
# Input: [2, 2, 0, 1, 2, 0]
# Output: [0 0 1 2 2 2]


def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0

    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:  # the case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1


def main():
    arr1 = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr1)
    print(arr1)

    arr2 = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr2)
    print(arr2)


main()
