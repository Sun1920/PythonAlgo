

def bucket_sort(raw):
    max_num = max(raw)

    bucket = [0] * (max_num + 1)

    for i in raw:
        bucket[i] += 1

    sort_nums = []

    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)

    return sort_nums


nums = [5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
print(bucket_sort(nums))
