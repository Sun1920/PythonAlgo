def bubble_sort(raw):
    for i in range(len(raw)):
        for j in range(i+1, len(raw)):
            if raw[i] > raw[j]:
                raw[i], raw[j] = raw[j], raw[i]


arr = [3, 5, 7, 8, 1, 3, 23, 222, 22, 5]
bubble_sort(arr)
print(arr)
