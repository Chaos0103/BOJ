n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

score = 0
size = 0
for n in data:
    score += size * n
    size += n

print(score)
