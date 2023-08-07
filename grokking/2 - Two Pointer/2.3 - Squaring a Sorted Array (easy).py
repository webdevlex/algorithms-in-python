# Question Given a sorted array, create a new array containing squares of all
# the number of the input array in the sorted order.

# Example 1:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# Example 2:
# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]


def make_squares(arr):
    lenOfArr = len(arr)

    left = 0
    right = lenOfArr - 1

    highest_square_idx = lenOfArr - 1
    squares = [-1] * lenOfArr

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            squares[highest_square_idx] = left_square
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1

        highest_square_idx -= 1

    return squares


def main():
    print("Squares:", str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares:", str(make_squares([-3, -1, 0, 1, 2])))


if __name__ == "__main__":
    main()
