INF = int(1e9)

n, m = map(int, input().split())
data = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            data[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

result = 1
min_value = INF
for a in range(1, n + 1):
    num = 0
    for b in range(1, n + 1):
        num += data[a][b]
    if num < min_value:
        min_value = num
        result = a

print(result)
