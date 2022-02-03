n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

data = sorted(data)
data = sorted(data, key=lambda x:x[1])

for i in data:
    print(*i)