from collections import deque, defaultdict


def bfs(graph: list[list], start_node: int, visited: list[bool]) -> list[int]:
    q = deque()
    q.append(start_node)
    visited[start_node] = True
    while q:
        node = q.popleft()
        for x in graph[node]:
            if not visited[x]:
                q.append(x)
                visited[x] = True

def solution(node_info: list[list], visited: list[bool]) -> int:
    answer = 0
    for x in range(1, len(node_info)):
        if not visited[x]:
            bfs(node_info, x, visited)
            answer += 1
    return answer

if __name__ == '__main__':
    n, m = map(int, input().split())
    node_info = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(m):
        key_node, connected_node = map(int, input().split())
        node_info[key_node].append(connected_node)
        node_info[connected_node].append(key_node)
    print(solution(node_info, visited))