def Count_Sort(array):
    ans = []
    count = [0]* (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1
    
    for i in range(len(count)):
        for j in range(count[i]):
            ans.append(i)
    return ans

'''
array = [6, 4, 1, 8, 5, 6, 4, 2, 1, 8, 7, 5, 4, 2, 3, 9, 7, ]
print(Count_Sort(array))
'''