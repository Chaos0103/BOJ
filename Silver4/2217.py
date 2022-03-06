n = int(input())
weights = [int(input()) for _ in range(n)]

weights.sort(reverse=True)
max_weight = weights[0]

for i in range(n):
    max_weight = max(max_weight, weights[i] * (i+1))

print(max_weight)
