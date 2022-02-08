import math

n = int(input())
data = list(map(int, input().split()))
array = [True for i in range(1001)]
array[1] = False

for i in range(2, int(math.sqrt(1001)) + 1):
    if array[i]:
        j = 2
        while i * j <= 1000:
            array[i * j] = False
            j += 1

result = 0
for num in data:
    if array[num]:
        result += 1

print(result)
