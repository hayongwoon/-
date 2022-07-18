from collections import deque, defaultdict


def bfs(graph, start_node):
    if not graph[start_node[0]][start_node[1]]:
        return False

    q = deque()
    q.append(start_node)
    graph[start_node[0]][start_node[1]] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        current_y, current_x = q.popleft()

        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]) and graph[ny][nx]:
                graph[ny][nx] = 0
                q.append((ny,nx))
                
    return True


t = int(input())
for _ in range(t):
    m, n, cabbage_num = map(int, input().split())

    xy_points_list = []
    for _ in range(cabbage_num):
        x, y = map(int, input().split())
        xy_points_list.append((x,y))


    graph = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if (i,j) in xy_points_list:
                graph[i][j] = 1

    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            result = bfs(graph, (i,j))
            if result:
                cnt += 1

    print(cnt)