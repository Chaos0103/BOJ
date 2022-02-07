from collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] > height and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


result = 1
for height in range(1, 101):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] > height and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    result = max(result, cnt)

print(result)
