n = int(input())
graph = dict()
for _ in range(n):
    root, left, right = input().split()
    graph[root] = [left, right]


def front(root):
    print(root, end='')
    if graph[root][0] != '.':
        front(graph[root][0])
    if graph[root][1] != '.':
        front(graph[root][1])


def mid(root):
    if graph[root][0] != '.':
        mid(graph[root][0])
    print(root, end='')
    if graph[root][1] != '.':
        mid(graph[root][1])


def back(root):
    if graph[root][0] != '.':
        back(graph[root][0])
    if graph[root][1] != '.':
        back(graph[root][1])
    print(root, end='')


front('A')
print()
mid('A')
print()
back('A')