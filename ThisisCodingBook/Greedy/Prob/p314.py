# Coins 의 동전으로 지불할 수 없는 최소 금액

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    if target < x:
        break
    target += x

print(target)

'''
4   
1 2 3 8
>> 7
'''