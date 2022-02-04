n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0

for i in range(n):
    result += sum(data[:i+1])

print(result)
