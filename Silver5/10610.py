num = input()

if '0' not in num:
    print(-1)
else:
    sum_value = 0
    for n in num:
        sum_value += int(n)

    if sum_value % 3 == 0:
        num = list(num)
        num.sort(reverse=True)
        print(''.join(num))
    else:
        print(-1)
