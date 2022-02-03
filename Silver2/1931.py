n = int(input())

data = []

for _ in range(n):
    s, e = map(int, input().split())
    data.append([s, e])

data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])

cnt = 0
end = 0

for s, e in data:
    if s >= end:
        cnt += 1
        end = e

print(cnt)