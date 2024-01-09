def solution(dirs):
    answer = set()
    x, y = 0, 0
    dp = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    for d in dirs:
        dx, dy = dp[d]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((nx, ny, x, y))
            answer.add((x, y, nx, ny))
            x = nx
            y = ny
    return len(answer) // 2
