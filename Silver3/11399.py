n = int(input())
datas = list(map(int, input().split()))

datas.sort()
result = 0

for i in range(n):
    for j in range(i+1):
        result += datas[j]

print(result)
