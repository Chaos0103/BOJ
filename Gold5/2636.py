from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def air():
    q = deque()
    q.append((0, 0))
    air_data[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and not air_data[nx][ny]:
                    air_data[nx][ny] = True
                    q.append((nx, ny))


time = -1
pre = 0
while True:
    time += 1
    count = 0
    air_data = [[False] * m for _ in range(n)]
    air()
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                if air_data[i+1][j] or air_data[i][j+1] or air_data[i-1][j] or air_data[i][j-1]:
                    data[i][j] = 0
                count += 1
    if count == 0:
        break
    pre = count

print(time)
print(pre)
