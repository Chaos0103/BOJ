n = list(input())
n.sort(reverse=True)

num = 0
for i in n:
    num += int(i)

if num % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))

# 3의 배수는 각 가리의 합이 3의 배수이다