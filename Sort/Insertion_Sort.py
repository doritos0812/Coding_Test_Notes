def Insertion_Sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

'''
array = [6, 3, 7, 1 ,2 ,9 ,5 ,4 ,8, 0]
Insertion_Sort(array)
print(array)
'''