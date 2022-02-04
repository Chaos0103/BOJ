line = input().split('-')

data = []

for d in line:
    num = 0
    ldata = d.split('+')
    for n in ldata:
        num += int(n)
    data.append(num)

result = data[0] * 2
for n in data:
    result -= n

print(result)
