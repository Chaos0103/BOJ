datas = input().split('-')

result = 0
for i in range(len(datas)):
    nums = datas[i].split('+')
    var = 0
    for j in range(len(nums)):
        var += int(nums[j])
    if i == 0:
        result = var
    else:
        result -= var

print(result)
