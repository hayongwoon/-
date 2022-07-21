from collections import deque


def bfs(graph, q):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<len(graph[0]) and 0<=ny<len(graph) and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

    return graph

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

result_graph = bfs(graph, q)

def solution(result_graph):
    answer = 0
    for i in range(len(result_graph)):
        for j in range(len(result_graph[0])):
            if not result_graph[i][j]:
                return -1
            else:
                answer = max(answer, result_graph[i][j])

    return answer - 1

print(solution(result_graph))