n = int(input())
Fear = map(int, input().split())

Fear = sorted(Fear, reverse= True)
count = 0
while Fear:
    Fear = Fear[Fear[0]:]
    count += 1

print(count)

'''
8
4 2 1 6 1 1 3 2
>> 3
'''