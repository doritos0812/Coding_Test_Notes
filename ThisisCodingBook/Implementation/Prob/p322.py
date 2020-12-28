data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))

'''
# My Original Code
n = input()
lst_str = []
lst_int = []

for i in n:
    k = ord(i)
    if k >= 65:
        lst_str.append(k)
    else:
        lst_int.append(k)

ans = ''.join([chr(x) for x in sorted(lst_str)]) + str(sum([int(x) - 48 for x in lst_int]))

print(ans)
'''
'''
K1KA5CB7
>> ABCKK13

AJKDLSI412K4JSJ9D
>> ADDIJJJKKLSS20
'''
