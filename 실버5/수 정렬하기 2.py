n = int(input())

data = [int(input()) for _ in range(n)]

data = sorted(data)

for num in data:
    print(num)