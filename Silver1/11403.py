INF = int(1e9)

n = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = data[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 or (graph[i][k] != 0 and graph[k][j] != 0):
                graph[i][j] = 1

for i in graph:
    print(*i)
