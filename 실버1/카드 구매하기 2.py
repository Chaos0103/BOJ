n = int(input())
data = [0] + list(map(int, input().split()))

d = [0] * 1001

for i in range(1, n+1):
    d[i] = data[i]
    for j in range(1, i+1):
        d[i] = min(d[i], d[i-j] + data[j])

print(d[n])