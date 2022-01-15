import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y, high, visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] > high and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x+1, y, high, visited)
        dfs(x-1, y, high, visited)
        dfs(x, y+1, high, visited)
        dfs(x, y-1, high, visited)
        return True
    return False


maxCnt = 0
for high in range(1, 101):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, high, visited):
                cnt += 1
    if cnt == 0:
        break
    if maxCnt < cnt:
        maxCnt = cnt

print(maxCnt)