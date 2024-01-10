from collections import deque


n, m= map(int, input().split())
maps = [input() for _ in range(n)]

def bfs(maps):
    q = deque() #패킹해서 넣어줘야 한다.   
    q.append([0,0])
    distance = [[0]*len(maps[0]) for _ in range(len(maps))] # 거리 기록
    distance[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    #해당 시작점에서 주변의 1이 없는지 확인
    while q:
        x, y = q.popleft()

        #시작점 기준으로 상하좌우의 노드를 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #방문하지 않는 노드이면서 범위 안에 있을 때
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == '1' and distance[nx][ny] == 0:
                q.append([nx, ny])
                distance[nx][ny] = distance[x][y] + 1 #시작점으로부터 거리를 더한다.

    return distance[-1][-1]


print(bfs(maps))