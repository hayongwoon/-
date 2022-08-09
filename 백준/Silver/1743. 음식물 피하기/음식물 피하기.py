from collections import deque


def bfs(start_node, graph):
    q = deque()
    q.append(start_node)
    graph[start_node[0]][start_node[1]] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<len(graph[0]) and 0<=ny<len(graph) and graph[ny][nx]:
                graph[ny][nx] = 0
                q.append((ny, nx))
    
    return cnt

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]

garbage_location = []
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1
    garbage_location.append((r-1, c-1))

answer = 0
for node in garbage_location:  
    if graph[node[0]][node[1]]: 
        result = bfs(node, graph)
        answer = max(answer, result)

print(answer)