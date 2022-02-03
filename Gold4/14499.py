top = 0
down = 0
front = 0
back = 0
left = 0
right = 0


n, m, x, y, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
order = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in order:
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    if i == 1 or i == 2:
        if i == 1:
            cycle = 1
        else:
            cycle = 3
        for _ in range(cycle):
            temp = down
            down = right
            right = top
            top = left
            left = temp
    else:
        if i == 3:
            cycle = 1
        else:
            cycle = 3
        for _ in range(cycle):
            temp = down
            down = back
            back = top
            top = front
            front = temp
    if data[nx][ny] == 0:
        data[nx][ny] = down
    else:
        down = data[nx][ny]
        data[nx][ny] = 0
    x, y = nx, ny
    print(top)
