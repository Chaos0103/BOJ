import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    elif x < 0:
        heapq.heappush(q, (-x, x))
    else:
        heapq.heappush(q, (x, x))
