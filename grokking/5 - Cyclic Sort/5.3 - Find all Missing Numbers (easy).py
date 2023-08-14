# Given an unsorted array with numbers from 1 to 'n' and possible duplicates,
# find the missing numbers.

# Example 1:
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: Array should have all numbers from 1 to 8; 4, 6, 7 are missing.

# Example 2:
# Input: [2, 4, 1, 2]
# Output: 3

# Example 3:
# Input: [2, 3, 2, 1]
# Output: 4


def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    missing_numbers = []

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
