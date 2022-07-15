from collections import deque, defaultdict


def bfs(graph, start_node):
    visited = []
    q = deque()
    q.append(start_node)

    while q:
        cur_node = q.popleft()
        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                q.append(adj_node)
                visited.append(adj_node)

    return visited


computer_number = int(input())
network_number = int(input())
graph = defaultdict(list)
for _ in range(network_number):
    node1, node2 = map(int, input().split())
    if node2 not in graph[node1]:
        graph[node1].append(node2)
    if node1 not in graph[node2]:
        graph[node2].append(node1)

print(len(bfs(graph, 1)) - 1)