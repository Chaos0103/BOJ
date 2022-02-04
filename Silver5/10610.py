str_num = list(input())
num = 0

if '0' not in str_num:
    print(-1)
else:
    for n in str_num:
        num += int(n)

    if num % 3 == 0:
        str_num.sort(reverse=True)
        print(''.join(str_num))
    else:
        print(-1)