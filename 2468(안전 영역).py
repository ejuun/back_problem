from collections import deque
N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

highest = max(map(max, land))

def bfs(rain, r, c):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  # 상 하 좌 우

    queue = deque()
    queue.append((r, c))

    if visited[r][c] == 0:
        return 0
    visited[r][c] = 0

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 0
    return 1

max_sector = 0

for rain in range(highest+1):

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if land[i][j] > rain:
                visited[i][j] = 1

    sector = 0

    for i in range(N):
        for j in range(N):
            if bfs(rain, i, j):
                sector += 1

    if max_sector < sector:
        max_sector = sector

print(max_sector)