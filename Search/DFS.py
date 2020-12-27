# Graph: 탐색을 진행할 그래프
# v: 현재 노드
# visited: 탐색 여부
def dfs(graph, v, visited): 
    visited[v] = True
    print(v, end=' ')
    # 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

'''
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

dfs(graph, 1, visited)

>> 1 2 7 6 8 3 4 5 
'''