from collections import deque


def bfs(graph, start_num, visited):
    q = deque()
    q.append(start_num)
    
    while q:
        cur_num = q.popleft()
        next_num = graph[cur_num]

        if next_num not in visited:
            visited.append(next_num)
            q.append(next_num)


t = int(input())
for _ in range(t):
    visited = []
    n = int(input())
    num_list = list(map(int, input().split()))

    graph = {idx: val for idx, val in enumerate(num_list, 1)}
    cnt = 0
    for i in range(1, n+1):
        if i not in visited:
            bfs(graph, i, visited)
            cnt += 1
    print(cnt)