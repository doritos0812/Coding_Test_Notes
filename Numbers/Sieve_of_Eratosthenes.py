def Eratosthenes(n):
    array = [True]*(n+1)
    for i in range(2,int(n**(1/2))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    for i in range(2, n+1):
        if array[i]:
            print(i)                      # Show Prime Numbers
            print(array[2:].count(True))  # Count of Prime Numbers

'''
Eratosthenes(10)
2 3 5 7 
4
'''
