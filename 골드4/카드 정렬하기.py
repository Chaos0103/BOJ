import heapq

n = int(input())
q = []
for _ in range(n):
    card = int(input())
    heapq.heappush(q, card)

result = 0
while len(q) != 1:
    num = heapq.heappop(q)
    num += heapq.heappop(q)
    heapq.heappush(q, num)
    result += num

print(result)