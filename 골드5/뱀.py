from collections import deque


def turn(x):
    global di
    di += x
    if di == 4:
        di = 0
    elif di == -1:
        di = 3


snack = deque()
snack.append([1, 1])
sec = 0

n = int(input())

apple = []
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    apple.append([x, y])

data = []
l = int(input())
for _ in range(l):
    x, c = input().split()
    data.append([x, c])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
di = 1
idx = 0
while True:
    sec += 1
    nx = snack[-1][0] + dx[di]
    ny = snack[-1][1] + dy[di]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        break
    if [nx, ny] in snack:
        break

    if [nx, ny] not in apple:
        snack.popleft()
    else:
        apple.remove([nx, ny])
    snack.append([nx, ny])

    if idx != l:
        if int(data[idx][0]) == sec:
            if data[idx][1] == 'D':
                turn(1)
            else:
                turn(-1)
            idx += 1

print(sec)

# 먹은 사과를 안지워서 반복적으로 먹음