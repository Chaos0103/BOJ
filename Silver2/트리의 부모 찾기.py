import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)


def dfs(tree, v, parents):
    for i in tree[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(tree, i, parents)


dfs(tree, 1, parents)

for i in range(2, n+1):
    print(parents[i])