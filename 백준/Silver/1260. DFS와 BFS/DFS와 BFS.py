from collections import deque, defaultdict


visited = []
def dfs(graph, start_node, visited_list):
    if start_node:
        print(start_node, end=' ')
    visited_list.append(start_node)
    for adj_node in graph[start_node]:
        if adj_node not in visited_list:
            dfs(graph, adj_node, visited_list)
            


def bfs(graph, start_node):
    q = deque()
    q.append(start_node)
    visited = [start_node]

    while q:
        cur_node = q.popleft()
        if cur_node:
            print(cur_node, end=' ')
        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                visited.append(adj_node)
                q.append(adj_node)


n, m, start_node = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    node1, node2 = map(int, input().split())
    if node2 not in graph[node1]:
        graph[node1].append(node2)
    if node1 not in graph[node2]:
        graph[node2].append(node1)

for key in graph.keys():
    graph[key].sort()


dfs(graph, start_node, visited)
print()
bfs(graph, start_node)
print()