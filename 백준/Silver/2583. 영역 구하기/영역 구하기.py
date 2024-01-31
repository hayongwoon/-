from collections import deque


def bfs(graph, start):
    y, x = start
    graph[y][x] = 1
    q = deque([start])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(graph[0]) and 0<=ny<len(graph) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append([ny, nx])
                cnt += 1
    return cnt


# 좌표 영역에 따른 그래프 만드는 함수, 영역 안 1, 아닌 곳은 0
def make_graph(m, n, k):
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = list(map(int, input().split()))
        for y in range(y1, y2):
            for x in range(x1, x2):
                graph[y][x] = 1
    return graph


def solution(m,n,k):
    answer = []
    graph = make_graph(m,n,k)
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:            
                answer.append(bfs(graph, [i, j]))
    return answer


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    answer = solution(m,n,k)
    answer.sort()
    print(len(answer))
    for x in answer:
        print(x, end=" ")
