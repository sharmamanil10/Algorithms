def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]


array = [4, 1, 6, 2, 8, 1]
selection_sort(array)

print(array)