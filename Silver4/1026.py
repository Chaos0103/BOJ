n = int(input())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

data = [-1] * n
array_A.sort()

for i in range(n):
    max_value = -1
    idx = 0
    for j in range(n):
        if array_B[j] > max_value and data[j] == -1:
            idx = j
            max_value = array_B[j]
    data[idx] = array_A[i]

for i in range(n):
    array_A[i] = data[i]

result = 0
for i in range(n):
    result += array_A[i] * array_B[i]

print(result)
