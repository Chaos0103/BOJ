import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


result = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)