n = int(input())
data = [input() for _ in range(n)]

data.sort(reverse=True, key= lambda x:len(x))
num = dict()

maxLen = len(data[0])
cnt = 9
idx = 0
for i in range(n):
    if data[i][idx] not in num:
        num[data[i][idx]] = cnt
        cnt -= 1
