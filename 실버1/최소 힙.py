import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


n = int(input())
data = []
flag = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(data) == 0:
            print(0)
        else:
            if flag == 1:
                data = heapsort(data)
            print(data.pop())
    else:
        data.append(num)
        flag = 1