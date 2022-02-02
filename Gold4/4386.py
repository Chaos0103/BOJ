from math import sqrt


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
result = 0

data = [list(map(float, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        cost = sqrt((data[i][0] - data[j][0])**2 + (data[i][1] - data[j][1])**2)
        edges.append((cost, i+1, j+1))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print('%.2lf' % result)
