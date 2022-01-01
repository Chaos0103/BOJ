n, d = map(int, input().split())
cnt = 0
for num in range(1, n+1):
    for c in str(num):
        if c == str(d):
            cnt += 1

print(cnt)