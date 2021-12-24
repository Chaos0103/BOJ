import sys

n = int(input())

data = [sys.stdin.readline().rstrip() for _ in range(n)]

data = sorted(data)
before = ''

for i in range(1, 51):
    for line in data:
        if len(line) == i:
            if before == line:
                continue
            else:
                before = line
                print(line)