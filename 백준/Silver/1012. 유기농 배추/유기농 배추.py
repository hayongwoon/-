from collections import deque

# maps, start를 인자로 넣으면 start와 주변 모든 1 -> 0 로 변환
def bfs(maps, start=[0,0]):
    q = deque()
    q.append(start)
    maps[start[0]][start[1]] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append([ny, nx])
    return maps

def solution(t: int) -> list[int]:
    answer = []
    for _ in range(t):
        m, n, k= map(int, input().split())
        # 스텝 1: 양배추 for문으로 maps 업데이트
        cabages = [list(map(int, input().split())) for _ in range(k)]
        maps = [[0]*m for _ in range(n)]
        for x in cabages:
            maps[x[1]][x[0]] = 1

        result = 0
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 1:
                    bfs(maps, [i, j])
                    result += 1
        answer.append(str(result))
    return '\n'.join(answer)

print(solution(int(input())))