from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(time[v])
            break
        for next in [v+1, v-1, v*2]:
            if 0 <= next <= 100000 and not time[next]:
                time[next] = time[v] + 1
                q.append(next)


n, k = map(int, input().split())
time = [0] * 1000001
bfs()
