cnt = 0
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    cnt += 1
    day = (v // p) * l
    if v % p != 0:
        if v%p > l:
            day += l
        else:
            day += v%p

    print(f"Case {cnt}: {day}")