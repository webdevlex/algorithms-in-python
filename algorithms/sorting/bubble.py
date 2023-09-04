def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


arr = [3, 1, 4, 2, 0]
print(f"input: {arr}")

bubbleSort(arr)
print(f"output: {arr}")
