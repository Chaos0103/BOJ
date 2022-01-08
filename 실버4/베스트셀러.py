n = int(input())
book = dict()
for _ in range(n):
    bookName = input()
    if bookName in book:
        book[bookName] += 1
    else:
        book[bookName] = 1

result = 0
maxCnt = 0
Key = list(book.keys())
for i in range(len(Key)):
    if maxCnt < book[Key[i]]:
        maxCnt = book[Key[i]]
        result = i
    elif maxCnt == book[Key[i]]:
        if Key[result] > Key[i]:
            maxCnt = book[Key[i]]
            result = i

print(Key[result])