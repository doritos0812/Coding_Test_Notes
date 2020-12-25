n, m = map(int, input().split())
data = []
small = []
for i in range(n):
    a = list(map(int, input().split()))
    data.append(a)
    small.append(min(a))
result = small.index(max(small))+1
print(result)


'''

3 3
3 1 2 
4 1 4
2 2 2
3

2 4
7 3 1 8
3 3 3 4
2
'''
