import heapq

n = int(input())
q = []
for i in range(n):
    data = list(map(int, input().split()))
    if i == 0:
        for j in range(n):
            heapq.heappush(q, data[j])
    else:
        for j in range(n):
            if q[0] < data[j]:
                heapq.heappop(q)
                heapq.heappush(q, data[j])

print(q[0])
