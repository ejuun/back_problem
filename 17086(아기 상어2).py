from collections import deque

N, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j):
    cnt = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for a in range(N):
        for b in range(M):
            if shark[a][b]:
                visited[a][b] = shark[a][b]

    if visited[i][j] == 1:
        return 0

    queue = deque()
    queue.append((i, j, cnt))
    visited[i][j] = 2

    while queue:
        x, y, cnt = queue.popleft()

        for row, col in ([-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]):
            nx = x + row
            ny = y + col
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = 2
                    new_cnt = cnt + 1
                    queue.append((nx, ny, new_cnt))
                elif visited[nx][ny] == 1:
                    return cnt+1
max_cnt = 0
for i in range(N):
    for j in range(M):
        a = bfs(i, j)
        if max_cnt <= a:
            max_cnt = a
print(max_cnt)