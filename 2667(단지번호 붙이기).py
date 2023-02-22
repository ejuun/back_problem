from collections import deque

N = int(input())
house = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1] #상하좌우

def bfs(r, c):
    queue = deque()
    cnt = 1
    queue.append((r, c))
    house[r][c] = 0
    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if house[nx][ny]:
                    queue.append((nx, ny))
                    house[nx][ny] = 0
                    cnt += 1
    return cnt

result = []
total = 0
for i in range(N):
    for j in range(N):
        if house[i][j]:
            a = bfs(i, j)
            result.append(a)
            total += 1
result.sort()
print(total)
for c in result:
    print(c)