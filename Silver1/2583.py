from collections import deque

m, n, k = map(int, input().split())
data = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            data[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append([x, y])
    data[x][y] = -1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0:
                    data[nx][ny] = -1
                    q.append([nx, ny])
                    cnt += 1
    return cnt


result = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)
