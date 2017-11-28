def quick_sort(a, first_index, last_index):
    if first_index < last_index:
        base = a[first_index]
        i = first_index
        j = last_index
        while i != j:
            while a[j] >= base and i < j:
                j -= 1
            while a[i] <= base and i < j:
                i += 1

            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        a[first_index] = a[i]
        a[i] = base

        quick_sort(a, first_index, last_index - 1)
        quick_sort(a, first_index + 1, last_index)
    else:
        return


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]

print("initial array:\n", arr)
quick_sort(arr, 0, len(arr) - 1)
print("result array:\n", arr)
