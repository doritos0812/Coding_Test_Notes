from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

    distance = [-1] * (n + 1)
    distance[x] = 0


def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs(graph, x, distance)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

'''
4 4 2 1
1 2
1 3
2 3
2 4
>> 4

4 3 2 1
1 2
1 3
1 4
>> -1

4 4 1 1
1 2
1 3
2 3
2 4
>> 2
>> 3
'''

