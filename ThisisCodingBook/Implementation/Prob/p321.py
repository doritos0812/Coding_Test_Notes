n = input()
t = len(n)//2
sum1 = 0
sum2 = 0
for i in range(t):
    sum1 += int(n[i])
for i in range(t, len(n)):
    sum2 += int(n[i])
if sum1 == sum2:
    print('Lucky')
else:
    print('Ready')

'''
123402
Lucky

7755
Ready
'''