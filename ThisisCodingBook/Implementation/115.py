n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1 ,-2), (2, -1), (1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2)]
result = 0
for step in steps:
    tmp_row = row + step[1]
    tmp_col = col + step[0]

    if tmp_col >= 1 and tmp_col <= 8 and tmp_row >= 1 and tmp_row <= 8:
        result += 1

print(result)


'''
a1
2

c5
8
'''