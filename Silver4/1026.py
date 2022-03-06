n = int(input())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

result = 0
for i in range(n):
    result += arrayA[i] * arrayB[i]

print(result)
