n = int(input())
data = list(map(int, input().split()))
data.sort()

front = 0
back = n-1
result = [0] * 2
value = int(2e9)

while True:
    if front >= back:
        break
    add = data[front] + data[back]
    if abs(value) > abs(add):
        value = add
        result[0] = front
        result[1] = back
    if add == 0:
        result[0] = front
        result[1] = back
        break
    elif add < 0:
        front += 1
    else:
        back -= 1

print(data[result[0]], data[result[1]])
