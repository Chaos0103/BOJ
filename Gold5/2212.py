n = int(input())
k = int(input())
data = list(map(int, input().split()))

if n <= k:
    print(0)
else:
    data.sort()
    gap = []
    for i in range(n-1):
        gap.append(data[i+1] - data[i])

    gap.sort()
    for _ in range(k-1):
        gap.pop()

    print(sum(gap))
