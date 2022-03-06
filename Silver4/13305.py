n = int(input())
line = list(map(int, input().split()))
oil = list(map(int, input().split()))

head, tail = 1, 0
result = 0

while head < n:
    if oil[tail] >= oil[head]:
        cnt = sum(line[tail:head])
        result += oil[tail] * cnt
        tail = head
    head += 1

cnt = sum(line[tail:head])
result += oil[tail] * cnt
print(result)
