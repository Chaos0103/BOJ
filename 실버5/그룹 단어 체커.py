import sys

n = int(input())

cnt = 0
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    c = 1
    for i in range(len(line)):
        s = 1
        for j in range(i, len(line)):
            if line[i] != line[j]:
                s = 0
            if line[i] == line[j] and s == 0:
                c = 0
                break
        if c == 0:
            break
    cnt += c

print(cnt)