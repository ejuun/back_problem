from collections import deque
N, M = map(int, input().split())
elec = [list(map(int, input())) for _ in range(N)]

def bfs(j):
    queue = deque()
    queue.append((0, j))
    visitied = [[0 for _ in range(M)] for _ in range(N)]
    visitied[0][j] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not elec[nx][ny] and not visitied[nx][ny]:
                    if nx == N-1:
                        return "YES"
                    queue.append((nx, ny))
                    visitied[nx][ny] = 1
    return "NO"

for j in range(M):
    if not elec[0][j]:
        if bfs(j) == "YES":
            print('YES')
            break
else:
    print('NO')