INF = int(1e9)

n, m = map(int, input().split())
data = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

result = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if data[a][b] != INF or data[b][a] != INF:
            cnt += 1
    if cnt == n-1:
        result += 1

print(result)
