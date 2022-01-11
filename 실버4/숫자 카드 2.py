from collections import Counter

n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

cnt = Counter(data1)

for num in data2:
    print(cnt[num], end=' ')