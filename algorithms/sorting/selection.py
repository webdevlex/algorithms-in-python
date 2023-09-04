def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            minIdx = i
            if arr[j] < arr[minIdx]:
                minIdx = j
            if minIdx != i:
                arr[minIdx], arr[i] = arr[i], arr[minIdx]


arr = [3, 1, 4, 2, 0]
print(f"input: {arr}")

selectionSort(arr)
print(f"output: {arr}")
