def bucket_sort(arr, decimal_place=0):
    buckets = [[] for _ in range(10)]

    for item in arr:
        idx = int(item * 10 ** (decimal_place + 1)) % 10
        buckets[idx].append(item)

    result = []
    for bucket in buckets:
        if len(bucket) > 1:
            bucket = bucket_sort(bucket, decimal_place + 1)

        for item in bucket:
            result.append(item)

    return result


arr = [
    0.78,
    0.17,
    0.39,
    0.26,
    0.72,
    0.94,
    0.21,
    0.12,
    0.23,
    0.68,
    0.53,
    0.77,
    0.19,
    0.15,
    0.99,
    0.45,
    0.09,
]
print(f"input: {arr}")

arr = bucket_sort(arr)
print(f"output: {arr}")
