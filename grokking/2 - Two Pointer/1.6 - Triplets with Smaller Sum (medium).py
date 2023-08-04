# Given an array arr of unsorted numbers and a target sum,
# count triplets (i, j, k) with arr[i] + arr[j] + arr[k] < target.
# Return the count of such triplets.

# Example 1:
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: Two triplets with sum < target: [-1, 0, 3], [-1, 0, 2]

# Example 2:
# Input: [-1, 4, 2, 1, 3], target=5
# Output: 4
# Explanation: Four triplets with sum < target:
# [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] < target:
                # Any number between 'left' and 'right' will also satisfy the condition.
                # So, we add 'right - left' to the count.
                count += right - left
                left += 1
            else:
                right -= 1

    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
