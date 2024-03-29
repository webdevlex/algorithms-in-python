def radix_sort(arr):
    max_digits = len(str(max(arr)))
    for place in range(max_digits):
        buckets = [[] for _ in range(10)]
        for number in arr:
            digit = (number // (10**place)) % 10
            buckets[digit].append(number)
        arr = [number for bucket in buckets for number in bucket]
    return arr


arr = [170, 45, 75, 90, 809, 24, 2, 66]
print(f"input: {arr}")

arr = radix_sort(arr)
print(f"output: {arr}")
