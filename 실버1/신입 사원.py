t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    for _ in range(n):
        p, t = map(int, input().split())
        data.append([p, t])

    data.sort(key=lambda x:x[0])

    rank = data[0][1]
    cnt = 1
    for i in range(1, n):
        if data[i][1] < rank:
            cnt += 1
            rank = data[i][1]
    print(cnt)

# 서류 오름차순, 면접으로 비교