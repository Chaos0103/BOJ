def d(n):
    A = n // 10000
    B = n // 1000 % 10
    C = n // 100 % 10
    D = n // 10 % 10
    E = n % 10
    return int(n+A+B+C+D+E)


data = [0] * 20000
for i in range(10000):
    data[d(i)] += 1

for i in range(1, 10000):
    if data[i] == 0:
        print(i)