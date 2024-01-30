from collections import deque


def bfs(graph, start):
    q = deque([start])
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    cnt = 1
    while q:
        v = q.popleft()
        for x in graph[v]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                cnt += 1
    return cnt
    
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
        
    for x, y in wires:
        graph[x].remove(y)
        graph[y].remove(x)

        answer = min(abs(bfs(graph, x) - bfs(graph, y)), answer)

        graph[x].append(y)
        graph[y].append(x)

    return answer