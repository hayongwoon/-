from collections import deque


def changing_graph_zero_one(graph, rain_amount):
    safety_graph = [[1]*len(graph[0]) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] <= rain_amount:
                safety_graph[i][j] = 0

    return safety_graph

def bfs(graph, start_node):
    q = deque()
    q.append(start_node)
    graph[start_node[0]][start_node[1]] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<len(graph[0]) and 0<=ny<len(graph) and graph[ny][nx]:
                q.append((ny,nx))
                graph[ny][nx] = 0

    return graph

def solution(graph, n):
    # 도시의 최대 높이를 구하여 강수량이 0~최대 높이까지 반복문을 통하여 최대 안전지대 영역의 갯수를 구할 예정
    max_height = 0
    for i in graph:
        max_height = max(max(i), max_height)

    answer = 0
    for rain_amount in range(max_height+1):
        new_graph = changing_graph_zero_one(graph, rain_amount) # 강수량에 따라 안전한 지역은 1, 잠긴 지역은 0으로 변환 그래프

        cnt = 0
        for i in range(n):
            for j in range(n):
                if new_graph[i][j]:
                    bfs(new_graph, (i,j)) # bfs함수를 통해 시작점 1이며 주변에 있는 1인 점을 0으로 바꾼다. -> 한 구역의 1인 구간을 0으로 변환
                    cnt += 1 # new_graph의 모든 1인 점이 0일 될 때까지 반복한 횟수가 안전지대 구역의 횟수이다.

        answer = max(cnt, answer)
    return answer

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(solution(graph, n))