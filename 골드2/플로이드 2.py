INF = int(1e9)


def path_f(a, b):
    if path[a][b] == 0:
        return []
    k = path[a][b]
    return path_f(a, k) + [k] + path_f(k, b)


n = int(input())
m = int(input())
data = [[INF] * (n+1) for _ in range(n+1)]
path = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if data[a][b] > c:
        data[a][b] = c

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            data[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if data[a][b] > data[a][k] + data[k][b]:
                data[a][b] = data[a][k] + data[k][b]
                path[a][b] = k

for a in range(1, n+1):
    for b in range(1, n+1):
        if data[a][b] == INF:
            print(0, end=' ')
        else:
            print(data[a][b], end=' ')
    print()

for a in range(1, n+1):
    for b in range(1, n+1):
        if data[a][b] in [0, INF]:
            print(0)
            continue
        rpath = [a] + path_f(a, b) + [b]
        print(len(rpath), *rpath)
