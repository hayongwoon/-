from collections import deque, defaultdict


def bfs(graph, start_num, target_num):
    q = deque()
    q.append(start_num)
    kavin_bacon = [0] * (len(graph) + 1)

    while q:
        cur_num = q.popleft()

        if cur_num == target_num:
            return kavin_bacon[cur_num]

        for adj_num in graph[cur_num]:
            if not kavin_bacon[adj_num]:
                kavin_bacon[adj_num] = kavin_bacon[cur_num] + 1
                q.append(adj_num)

graph = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
answer = []
for i in range(1, n+1):
    kavin_cnt = 0
    for j in range(1, n+1):
        kavin_cnt += bfs(graph, i, j)

    answer.append(kavin_cnt)
print(answer.index(min(answer)) + 1)