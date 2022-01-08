from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


bfs()
result = 0
for i in range(n):
    if 0 in graph[i]:
        print(-1)
        exit()
    m = max(graph[i])
    result = max(m, result)

print(result-1)

# 하나씩 따로 비교하는것이 아닌, 전부 큐에 넣고 한번에 실행