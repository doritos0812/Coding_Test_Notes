from itertools import combinations

n, m = map(int, input().split())
hs = []
ck = []
for x in range(n):
    st = list(map(int, input().split()))
    for y in range(n):
        if st[y] == 1:
            hs.append([x, y])
        if st[y] == 2:
            ck.append([x, y])

chosen_ck = combinations(ck, m)

def get_len(hs, ck):
    result = 0
    for x,y in hs:
        tmp = 1e9
        for a,b in ck:
            tmp = min(tmp, abs(x-a) + abs(y-b))
        result += tmp
    return result

lng = [get_len(hs, ck) for ck in chosen_ck]

print(min(lng))


'''
<My Original Code>

from itertools import combinations
n,m = map(int,input().split())
streets = []
for _ in range(n):
    streets.append(list(map(int, input().split())))

chickens = []
count = 0
for x in range(n):
    for y in range(n):
        if streets[x][y] == 2:
            count += 1
            chickens.append([x, y])

chickens = list(combinations(chickens, count - m))

togo = []
for chicken in chickens:
    for way in chicken:
        streets[way[0]][way[1]] = 0
    length = []
    for a in range(n):
        for b in range(n):
            if streets[a][b] == 1:
                low = 9999999
                for x in range(n):
                    for y in range(n):
                        if streets[x][y] == 2:
                            if abs(x-a) + abs(y-b) <= low:
                                low = abs(x-a) + abs(y-b)
                length.append(low)
    togo.append(sum(length))
        
    for way in chicken:
        streets[way[0]][way[1]] = 2

print(min(togo))
'''


'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
>> 5

5 2 
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
>> 10

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
>> 11
'''
