n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

data.sort()

for i in data:
    print(*i)