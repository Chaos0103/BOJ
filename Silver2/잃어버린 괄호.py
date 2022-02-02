line = input().split('-')

data = []

for l in line:
    num = 0
    sdata = l.split('+')
    for n in sdata:
        num += int(n)
    data.append(num)

result = data[0]
for i in range(1, len(data)):
    result -= data[i]

print(result)

# 알고리즘은 맞았는데 구현에서 틀림
# split 활용
# eval은 0으로 시작하면 적용 불가