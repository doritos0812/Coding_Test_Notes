n = input()
n = [int(x) for x in n]
add = int(n[0])
for i in range(1,len(n)):
    if add + n[i] < add * n[i]:
        add *= n[i]
    else:
        add += n[i]

print(add)

'''
02984
>> 576

567
>> 210
'''