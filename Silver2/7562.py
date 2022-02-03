from collections import deque

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]


def bfs():
    visited = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    visited[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        if x == goal_x and y == goal_y:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited[goal_x][goal_y]


for _ in range(int(input())):
    n = int(input())
    now_x, now_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    print(bfs())
