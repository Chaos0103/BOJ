n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 1
for weight in data:
    if result < weight:
        break
    result += weight

print(result)
