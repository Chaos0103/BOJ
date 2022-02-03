n = int(input())
data = list(map(int, input().split()))
x = int(input())

left = 0
right = n-1
data.sort()
cnt = 0
while left < right:
    num = data[left] + data[right]
    if x == num:
        cnt += 1
        left += 1
    elif num > x:
        right -= 1
    else:
        left += 1
print(cnt)