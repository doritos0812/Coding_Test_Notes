def Sum_Interval(arr, n):
    arr_len = len(arr)
    count = 0
    interval_sum = 0
    end = 0
    for start in range(arr_len):
        while interval_sum < n and end < arr_len:
            interval_sum += arr[end]
            end += 1
        if interval_sum == n:
            count += 1
            print('Add from Index {0} to {1} is {2}'.format(start, end-1,n)) # Delete if you want only count
        interval_sum -= arr[start]
    return count

'''
arr = [1,3,2,5,1,2,6,2,4,2,6]
n = 6
print(Sum_Interval(arr, n))


Add from Index 0 to 2 is 6
Add from Index 3 to 4 is 6
Add from Index 6 to 6 is 6
Add from Index 7 to 8 is 6
Add from Index 8 to 9 is 6
Add from Index 10 to 10 is 6
6
'''