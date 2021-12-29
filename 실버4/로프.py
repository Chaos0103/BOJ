n = int(input())
data = [int(input()) for _ in range(n)]

data.sort()

result = 0
for w in data:
    result = max(result, w*n)
    n -= 1

print(result)