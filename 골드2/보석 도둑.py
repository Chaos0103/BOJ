import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = []
for _ in range(n):
    heapq.heappush(q, list(map(int, input().split())))
bag = [int(input()) for _ in range(k)]
bag.sort()

result = 0
data = []
for b in bag:
    while q and b >= q[0][0]:
        w, v = heapq.heappop(q)
        heapq.heappush(data, -v)
    if data:
        result -= heapq.heappop(data)

print(result)
