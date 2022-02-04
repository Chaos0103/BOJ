n = int(input())
lopes = [int(input()) for _ in range(n)]

lopes.sort(reverse=True)

result = lopes[0]
cnt = 1
for lope in lopes:
    result = max(result, lope * cnt)
    cnt += 1

print(result)
