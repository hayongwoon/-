from collections import deque


def bfs(graph, start_node):
    if graph[start_node[0]][start_node[1]] == "0":
        return False

    visited = []
    q = deque()
    q.append(start_node)
    visited.append(start_node)
    graph[start_node[0]][start_node[1]] = "0"

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < len(graph[0]) and 0<= ny < len(graph) and graph[ny][nx] == "1":
                if (ny, nx) not in visited:
                    graph[ny][nx] = "0"
                    visited.append((ny, nx))
                    q.append((ny, nx))

    return visited


n = int(input())
graph = [list(input()) for _ in range(n)]

cnt = 0
answer = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j]:
            result = bfs(graph, (i, j))
            if result:
                cnt += 1
                answer.append(len(result))
print(cnt)
answer.sort()
for i in answer:
    print(i)