import sys

n, m = map(int, input().split())
listen = set(sys.stdin.readline().rstrip() for _ in range(n))
look = set(sys.stdin.readline().rstrip() for _ in range(m))

result = sorted(list(listen & look))
print(len(result))
for name in result:
    print(name)