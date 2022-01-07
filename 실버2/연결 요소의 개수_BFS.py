from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


node, link = map(int, input().split())
graph = [[] for _ in range(node+1)]
for _ in range(link):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (node+1)
cnt = 0
for i in range(1, node+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)