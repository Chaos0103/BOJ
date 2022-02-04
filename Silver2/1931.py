n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort()
start, end = data[0]
result = 1

for i in range(1, n):
    if end <= data[i][0]:
        start, end = data[i]
        result += 1
    elif start <= data[i][0] and data[i][1] <= end:
        start, end = data[i]

print(result)
