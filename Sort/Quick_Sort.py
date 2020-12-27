def Quick_Sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return Quick_Sort(left_side) + [pivot] + Quick_Sort(right_side)


'''
array = [6, 3, 7, 1 ,2 ,9 ,5 ,4 ,8, 0]
print(Quick_Sort(array))
'''