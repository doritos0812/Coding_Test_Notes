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
N을 K로 나누거나 N에 1을 빼거나
행동한 최소 횟수를 return

5 2
3

25 5
2

23625142623464234 345
1055
'''
