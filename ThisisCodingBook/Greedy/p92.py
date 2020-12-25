n,m,k = map(int,input().split())
data = list(map(int,input().split()))
while len(data) != n:
    print("Wrong Length of Data")
    data = list(map(int,input().split()))
data.sort()
first = data[-1]
second = data[-2]
sum = 0
while True:
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)

'''
N 길이의 숫자 배열에서 
M번 더한 수의 합이 가장 클 경우
단, K번 연속 중복은 안됨

ex)
4 6 2
4 2 6 3
32
'''

