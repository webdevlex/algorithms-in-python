def insertionSort(arr):
    for i in range(0, len(arr) - 1):
        currentIdx = i
        while currentIdx >= 0 and arr[currentIdx + 1] < arr[currentIdx]:
            arr[currentIdx + 1], arr[currentIdx] = arr[currentIdx], arr[currentIdx + 1]
            currentIdx -= 1


arr = [3, 1, 4, 2, 0]
print(f"input: {arr}")

insertionSort(arr)
print(f"output: {arr}")
