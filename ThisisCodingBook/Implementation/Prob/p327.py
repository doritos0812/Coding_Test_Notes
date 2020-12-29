n = int(input())
k = int(input())
apples = []
for i in range(k):
    apples.append(list(map(int,input().split())))
l = int(input())
way = []
for i in range(l):
    way.append(list(input().split()))
    way[i][0] = int(way[i][0])

stage = [[0] * n for _ in range(n)]
for x,y in apples:
    stage[x-1][y-1] = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dummy = [3, [0, 0]]

flag = 1

def check(dummy):
    if dummy[-1][0] <= -1 or dummy[-1][0] >= n:
        return False
    if dummy[-1][1] <= -1 or dummy[-1][1] >= n:
        return False
    if dummy[-1][0] == dummy [1][0] and dummy[-1][1] == dummy [1][1]:
        return False
    return True

def go(dummy):
    global flag
    nx = dummy[-1][0] + dx[dummy[0]]
    ny = dummy[-1][1] + dy[dummy[0]]
    dummy.append([nx, ny])
    if check(dummy):
        if stage[nx][ny] != 1:
            dummy.pop(1)
    else:
        flag = 0


def turn(dummy, direct):
    '''
    <My Original>
    if direct == 'L':
        dummy[0] -= 1
        if dummy[0] == -1:
            dummy[0] = 3
    elif direct == 'D':
        dummy[0] += 1
        if dummy[0] == 4:
            dummy[0] = 0
    '''
    if direct == 'L':
        dummy[0] = (dummy[0] - 1) % 4
    elif direct == 'D':
        dummy[0] = (dummy[0] + 1) % 4

count = 0

while True:
    if way:
        if way[0][0] == count:
            turn(dummy, way[0][1])
            way.pop(0)
    go(dummy)
    count += 1
    if not flag:
        break

print(count)


'''
6 
3
3 4
2 5
5 3
3
3 D
15 L
17 D

>> 9


10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

>> 21


10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

>> 13


'''