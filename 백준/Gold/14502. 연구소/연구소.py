from collections import deque
import copy

def bfs(graph, q: deque):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(graph[0]) and 0<=ny<len(graph) and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append([ny, nx])
    
    global answer
    cnt = 0 
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)


def make_wall(cnt):
    if cnt == 3:
        temp_graph = copy.deepcopy(graph)
        q = deque()
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if temp_graph[i][j] == 2:
                    q.append([i, j])
        bfs(temp_graph, q)
        return

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
make_wall(0)
print(answer)