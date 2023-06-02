def magicIndex(arr):
    return magicIndexHelper(arr, 0, len(arr) - 1)


def magicIndexHelper(arr, begin, end):
    if begin <= end:
        mid = (begin + end) // 2

        print(mid, arr[mid])
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            return magicIndexHelper(arr, mid + 1, end)
        else:
            return magicIndexHelper(arr, begin, mid - 1)

    return -1


arr = [-5, 0, 1, 3]
print(magicIndex(arr))
