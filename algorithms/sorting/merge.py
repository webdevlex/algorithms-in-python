def merge_sort(arr):
    helper = [0] * len(arr)
    merge_sort_helper(arr, helper, 0, len(arr) - 1)


def merge_sort_helper(arr, helper, low, high):
    if low < high:
        middle = low + ((high - low) // 2)
        merge_sort_helper(arr, helper, low, middle)
        merge_sort_helper(arr, helper, middle + 1, high)
        merge(arr, helper, low, middle, high)


def merge(arr, helper, low, middle, high):
    for i in range(low, high + 1):
        helper[i] = arr[i]

    helper_left = low
    helper_right = middle + 1
    current = low

    while helper_left <= middle and helper_right <= high:
        if helper[helper_left] <= helper[helper_right]:
            arr[current] = helper[helper_left]
            helper_left += 1
        else:
            arr[current] = helper[helper_right]
            helper_right += 1
        current += 1

    remaining = middle - helper_left
    for i in range(remaining + 1):
        arr[current + i] = helper[helper_left + i]
