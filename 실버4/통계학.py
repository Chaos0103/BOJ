from collections import Counter

n = int(input())
data = [int(input()) for _ in range(n)]

result = sum(data) / n
print(round(result))

data = sorted(data)
print(data[n//2])

if n == 1:
    print(data[0])
else:
    cnt = Counter(data)
    num = cnt.most_common(2)
    if num[0][1] == num[1][1]:
        print(num[1][0])
    else:
        print(num[0][0])

print(data[-1] - data[0])