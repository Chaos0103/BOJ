import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
start = 1
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijsktra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


distance = [INF] * (n + 1)
dijsktra(start)
oneToTwo = distance[v1]
twoToOne = distance[v2]
distance = [INF] * (n + 1)
dijsktra(v1)
oneToTwo += distance[v2]
twoToOne += distance[n]
distance = [INF] * (n + 1)
dijsktra(v2)
twoToOne += distance[v1]
oneToTwo += distance[n]

if oneToTwo >= INF and twoToOne >= INF:
    print(-1)
else:
    print(min(oneToTwo, twoToOne))
