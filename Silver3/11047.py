n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.reverse()
result = 0

for coin in coins:
    result += k // coin
    k %= coin

print(result)
