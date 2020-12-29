def check(frame):
    for x, y, stuff in frame:
        if frame == 0:
            if y == 0 or [x-1, y, 1] in frame or [x, y, 1] in frame or [x, y - 1, 0] in frame:
                continue
            return False
        elif stuff == 1:
            if [x, y-1, 0] in frame or [x+1, y-1, 0] in frame or ([x-1,y,1] in frame and [x+1, y, 1] in frame):
                continue
            return False
    return True

        


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not check(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not check(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)
        

'''
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))


>> [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
'''