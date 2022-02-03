t = int(input())

data = [int(input()) for _ in range(t)]

M = max(data)

d = [0] * (M+1)
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, M+1):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009

for n in data:
    print(d[n])