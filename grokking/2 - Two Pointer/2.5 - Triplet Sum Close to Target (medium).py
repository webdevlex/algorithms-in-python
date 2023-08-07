# Question: Given an array of unsorted numbers and a target number, find a
# triplet in the array whose sum is as close to the target number as possible,
# return the sum of the triplet. If there are more than one such triplet,
# return the sum of the triplet with the smallest sum.


def search_triplet(arr, target_sum):
    arr.sort()
    smallest_difference = float("inf")

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]

            if target_diff == 0:
                return target_sum - target_diff  # return sum of the triplet

            if abs(target_diff) < abs(smallest_difference):
                smallest_difference = target_diff  # save the closest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1

    return target_sum - smallest_difference


if __name__ == "__main__":
    vec = [-2, 0, 1, 2]
    print(search_triplet(vec, 2))

    vec = [-3, -1, 1, 2]
    print(search_triplet(vec, 1))

    vec = [1, 0, 1, 1]
    print(search_triplet(vec, 100))
