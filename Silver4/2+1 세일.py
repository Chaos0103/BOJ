n = int(input())
data = [int(input()) for _ in range(n)]

data.sort(reverse=True)

result = 0
for i in range(n):
    if (i+1)%3==0:
        continue
    result += data[i]

print(result)