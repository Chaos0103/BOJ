# 2941번

import sys

data = {'c=':1, 'c-':1, 'dz=':2, 'd-':1, 'lj':2, 'nj':2, 's=':1, 'z=':1}

line = sys.stdin.readline().rstrip()

cnt = 0
for i in range(len(line)-1):
    if line[i:i+2] in data:
        cnt += data[line[i:i+2]]
    elif line[i:i+3] in data:
        cnt += data[line[i:i+3]]

print(cnt)