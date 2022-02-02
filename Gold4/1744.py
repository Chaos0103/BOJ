n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

positive_num = []
negative_num = []
zero_cnt = 0
result = 0

for num in data:
    if num < 0:
        negative_num.append(num)
    elif num == 0:
        zero_cnt += 1
    elif num == 1:
        result += 1
    else:
        positive_num.append(num)

if positive_num:
    if len(positive_num) % 2 == 1:
        result += positive_num[0]
        for i in range(1, len(positive_num), 2):
            result += positive_num[i] * positive_num[i+1]
    else:
        for i in range(0, len(positive_num), 2):
            result += positive_num[i] * positive_num[i+1]

if negative_num:
    if len(negative_num) % 2 == 1:
        if zero_cnt == 0:
            result += negative_num[-1]
        for i in range(0, len(negative_num) - 1, 2):
            result += negative_num[i] * negative_num[i + 1]
    else:
        for i in range(0, len(negative_num), 2):
            result += negative_num[i] * negative_num[i+1]

print(result)
