import sys

line = sys.stdin.readline().rstrip()
line += ' '
Xcnt = 0
result = ''
for i in range(len(line)):
    if line[i] == 'X':
        Xcnt += 1
    else:
        if Xcnt%2 == 1:
            result = '-1'
            break
        result += 'AAAA' * (Xcnt // 4)
        if Xcnt % 4 != 0:
            result += 'BB'
        if line[i] == '.':
            result += '.'
        Xcnt = 0

print(result)