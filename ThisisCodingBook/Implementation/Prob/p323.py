def solution(s):
    answers = []
    for k in range(1, (len(s)//2)+1):
        answer = ''
        lst = [s[i:i+k] for i in range(0,len(s),k)]
        count = 1
        for p in range(len(lst)-1):
            if lst[p] == lst[p+1]:
                count += 1
            else:
                if count > 1:
                    answer += str(count)
                answer += lst[p]
                count = 1
        if count > 1:
            answer += str(count)
        answer += lst[-1]
        answers.append(len(answer))
    return min(answers)

'''
s = "aabbaccc"
print(solution(s))

s = "ababcdcdababcdcd"
print(solution(s))

s = "abcabcabcabcdededededede"
print(solution(s))

s = "xababcdcdababcdcd"
print(solution(s))

>>
7
9
14
17
'''