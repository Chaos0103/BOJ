from collections import deque

r, c, t = map(int, input().split())
datas, air, q = [], [], deque()

for i in range(r):
    data = list(map(int, input().split()))
    datas.append(data)
    for j in range(c):
        if data[j] == -1:
            air.append((i, j))
        elif data[j] != 0:
            q.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def pos_move(x, y):
    count = 0
    now = datas[x][y] // 5
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if datas[nx][ny] != -1:
                count += 1
                now_pos[nx][ny] += now
    datas[x][y] -= now * count



up_air = [(-1, 0), (0, 1), (1, 0), (0, -1)]
down_air = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(t):
    # 확산
    now_pos = [[0] * c for _ in range(r)]
    while q:
        x, y = q.popleft()
        pos_move(x, y)
    for i in range(r):
        for j in range(c):
            datas[i][j] += now_pos[i][j]

    # 공기청정기
    idx = 0
    x, y = air[0]
    x -= 1
    while True:
        nx = x + up_air[idx][0]
        ny = y + up_air[idx][1]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or nx > air[0][0]:
            idx += 1
            continue
        if datas[nx][ny] == -1:
            datas[x][y] = 0
            break
        datas[x][y] = datas[nx][ny]
        x, y = nx, ny
    idx = 0
    x, y = air[1]
    x += 1
    while True:
        nx = x + down_air[idx][0]
        ny = y + down_air[idx][1]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or nx < air[1][0]:
            idx += 1
            continue
        if datas[nx][ny] == -1:
            datas[x][y] = 0
            break
        datas[x][y] = datas[nx][ny]
        x, y = nx, ny
    for i in range(r):
        for j in range(c):
            if datas[i][j] > 0:
                q.append((i, j))

result = 2
for data in datas:
    result += sum(data)
print(result)
