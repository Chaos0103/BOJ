n = int(input())
data1 = set(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

for n in data2:
    if n in data1:
        print(1, end=' ')
    else:
        print(0, end=' ')