n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
part_sum = 0
end = 0

for start in range(n):
    while part_sum < m and end < n:
        part_sum += data[end]
        end += 1
    if part_sum == m:
        result += 1
    part_sum -= data[start]

print(result)
