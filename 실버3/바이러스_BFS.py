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


n = int(input())
graph = [[] for _ in range(n+1)]
link = int(input())
for _ in range(link):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
bfs(graph, 1, visited)
print(visited.count(True) - 1)