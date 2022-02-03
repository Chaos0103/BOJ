from collections import deque

m, n, h = map(int, input().split())
data = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        data[i].append(list(map(int, input().split())))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and data[nx][ny][nz] == 0:
            data[nx][ny][nz] = data[x][y][z] + 1
            q.append((nx, ny, nz))

result = 0
for i in range(h):
    for j in range(n):
        if 0 in data[i][j]:
            print(-1)
            exit()
        m = max(data[i][j])
        result = max(m, result)

print(result - 1)
