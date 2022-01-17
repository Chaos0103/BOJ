data = dict()
n = int(input())
for _ in range(n):
    card = int(input())
    if card in data:
        data[card] += 1
    else:
        data[card] = 1

data = sorted(data.items(), key=lambda item:(-item[1], item[0]))
print(data[0][0])