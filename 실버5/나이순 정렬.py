n = int(input())
data = []
for _ in range(n):
    age, name = input().split()
    data.append([int(age), name])

data = sorted(data, key=lambda x:x[0])

for i in data:
    print(*i)