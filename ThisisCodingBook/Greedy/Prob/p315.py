'''
# MY Original Code

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int,input().split()))

comb = [x for x in list(combinations(data, 2)) if x[0] != x[1]]
print(len(comb))
'''
n, m = map(int, input().split())
data = list(map(int,input().split()))

array = [0]*11
for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)

'''
8 5
1 5 4 3 2 4 5 2

>> 25
'''
