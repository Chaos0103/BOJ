import heapq

n = int(input())
q = []
for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(q, (d, w))

data = []
for _ in range(n):
    d, w = heapq.heappop(q)
    if d == len(data):
        heapq.heappop(data)
    heapq.heappush(data, (w, d))

result = 0
while data:
    w = heapq.heappop(data)[0]
    result += w

print(result)
