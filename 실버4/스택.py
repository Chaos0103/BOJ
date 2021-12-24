import sys

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if order == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif order == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(order[5:]))