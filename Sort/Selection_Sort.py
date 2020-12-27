def Selection_Sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

'''
array = [6, 3, 7, 1 ,2 ,9 ,5 ,4 ,8, 0]
Selection_Sort(array)
print(array)
'''