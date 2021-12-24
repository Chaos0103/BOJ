from itertools import permutations

n, m = map(int, input().split())

data = [i for i in range(1, n+1)]

result = list(permutations(data, m))

for num in result:
    print(*num)