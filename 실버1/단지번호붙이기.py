n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))


def dfs(x, y, cnt):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == '1':
        graph[x][y] = str(cnt)
        dfs(x+1, y, cnt)
        dfs(x-1, y, cnt)
        dfs(x, y+1, cnt)
        dfs(x, y-1, cnt)
        return True
    return False

cnt = 2
aCnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, cnt):
            aCnt += 1
            cnt += 1

print(aCnt)
cnt = [0] * aCnt
for i in range(n):
    for j in range(aCnt):
        cnt[j] += graph[i].count(str(j+2))
cnt.sort()
for n in cnt:
    print(n)