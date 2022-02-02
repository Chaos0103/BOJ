import sys
n = int(sys.stdin.readline())
data = set()
for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'add':
        data.add(int(line[1]))
    elif line[0] == 'remove':
        data.discard(int(line[1]))
    elif line[0] == 'check':
        if int(line[1]) in data:
            print(1)
        else:
            print(0)
    elif line[0] == 'toggle':
        if int(line[1]) in data:
            data.discard(int(line[1]))
        else:
            data.add(int(line[1]))
    elif line[0] == 'all':
        data = set([i for i in range(1, 21)])
    elif line[0] == 'empty':
        data = set()

# Python3 통과, PyPy3 메모리 초과
# remove는 없는 원소를 지울 때 에러 발생