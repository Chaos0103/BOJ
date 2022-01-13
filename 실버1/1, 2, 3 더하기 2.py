from itertools import product

n, k = map(int, input().split())
data = [1, 2, 3]
array = []
for i in range(n, 0, -1):
    result = list(product(data, repeat=i))
    for d in result:
        if sum(d) == n:
            array.append(d)
    if len(array) > k:
        break

array.sort()
try:
    for i in range(len(array[k-1])-1):
        print(array[k-1][i],end='+')
    print(array[k-1][-1])
except:
    print(-1)