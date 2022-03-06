n = int(input())

datas = []
for _ in range(n):
    a, b = map(int, input().split())
    datas.append((a, b))

datas = sorted(datas, key=lambda x:x[0])
datas = sorted(datas, key=lambda x:x[1])

start, end = datas[0]
result = 1
for i in range(1, n):
    if end <= datas[i][0]:
        start, end = datas[i]
        result += 1

print(result)