import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(n)]

data.sort(reverse=True, key=lambda x:len(x))
cnt = dict()

l = len(data[0])
for i in range(l):
    for j in cnt:
        cnt[j] *= 10
    for line in data:
        if l-i > len(line):
            continue
        idx = i - (l - len(line))
        if line[idx] in cnt:
            cnt[line[idx]] += 1
        else:
            cnt[line[idx]] = 1

cntSort = sorted(cnt.items(), key=lambda item:item[1], reverse=True)
num = 9
result = 0

for idx in range(len(cntSort)):
    result += num * cntSort[idx][1]
    num -= 1

print(result)