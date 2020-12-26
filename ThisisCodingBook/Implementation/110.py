n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direct = ['L', 'R', 'U', 'D']

for data in plans:
    for i in range(len(direct)):
        if data == direct[i]:
            tx = x + dx[i]
            ty = y + dy[i]
        
    if tx < 1 or tx > n or ty < 1 or ty > n:
        continue
    x, y = tx, ty

print(x, y)

'''
3
R R R R R L U U D

>> 2 2
'''

'''
<My Original Code>
n = int(input())
data = input().split()
loca_X = 1
loca_Y = 1
for i in data:
    if i == 'R':
        if loca_Y == n:
            continue
        loca_Y += 1
    elif i == 'L':
        if loca_Y == 1:
            continue
        loca_Y -= 1
    elif i == 'U':
        if loca_X == 1:
            continue
        loca_X -= 1
    elif i == 'D':
        if loca_X == n:
            continue
        loca_X += 1
    else:
        print('Wrong Input')

print(loca_X, loca_Y)
'''