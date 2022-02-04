n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
result = 0

data.reverse()

for coin in data:
    num = k // coin
    if num > 0:
        result += num
        k %= coin
    if k == 0:
        break

print(result)
