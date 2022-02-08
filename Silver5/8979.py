n, k = map(int, input().split())
datas = []
g = []
for _ in range(n):
    data = list(map(int, input().split()))
    datas.append(data)
    if data[0] == k:
        g = data

datas.sort(key=lambda x: (-x[1], -x[2], -x[3]))

result = 1
for data in datas:
    if data[0] == k:
        break
    if g[1] == data[1] and g[2] == data[2] and g[3] == data[3]:
        break
    result += 1

print(result)
