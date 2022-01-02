n = int(input())
l = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
node = 0
idx = 1
while idx < n:
    if cost[node] >= cost[idx]:
        cnt = sum(l[node:idx])
        result += cost[node] * cnt
        node = idx
    idx += 1

print(result)