import sys
from collections import deque


def turn_right(Cdata):
    Cdata.appendleft(Cdata.pop())


def turn_left(Cdata):
    Cdata.append(Cdata.popleft())


result = 0
score = [0, 1, 2, 4, 8]

data = list()
data.append(deque(''))
for _ in range(4):
    data.append(deque(input()))

k = int(input())
for _ in range(k):
    num, di = map(int, input().split())
    check = [0] * 5
    check[num] = di
    # 돌아갈 바퀴 체크
    for i in range(num-1, 0, -1):
        if data[i][2] != data[i+1][6]:
            check[i] = check[i+1] * -1
    for i in range(num+1, 5):
        if data[i][6] != data[i - 1][2]:
            check[i] = check[i-1] * -1
    for i in range(1, 5):
        if check[i] == 1:
            turn_right(data[i])
        elif check[i] == -1:
            turn_left(data[i])

for i in range(1, 5):
    if data[i][0] == '1':
        result += score[i]

print(result)