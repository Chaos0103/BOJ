n = int(input())
data = [int(input()) for _ in range(n)]

data.sort()

result = 0

for i in range(1, n+1):
    if data[i-1] != i:
        dif = data[i-1] - i
        if dif < 0:
            dif *= -1
        result += dif

print(result)