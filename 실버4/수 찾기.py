n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))
data1.sort()


def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

    
for num in data2:
    if binary_search(data1, num, 0, n-1):
        print(1)
    else:
        print(0)