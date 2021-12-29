n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]

data.reverse()

cnt = 0
for coin in data:
    if coin <= k:
        cnt += k // coin
        k %= coin
    if k == 0:
        break

print(cnt)