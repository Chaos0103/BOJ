from collections import deque

t = int(input())
for _ in range(t):
    order = input()
    p = int(input())
    arr = input()[1:-1].split(',')
    num = deque(arr)
    flag = 0
    for c in order:
        if c == 'R':
            flag += 1
        elif c == 'D':
            p -= 1
            if p == -1:
                break
            if flag % 2 == 0:
                num.popleft()
            else:
                num.pop()

    if flag % 2 == 1:
        num.reverse()
    if p == -1:
        print('error')
    else:
        print('['+','.join(num)+']')