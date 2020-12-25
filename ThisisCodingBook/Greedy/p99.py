n, k = map(int, input().split())
count = 0
while (n != 1):
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)


'''
5 2
3

25 5
2

23625142623464234 345
1055
'''