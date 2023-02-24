from collections import deque

N, M, K = map(int, input().split())

trash = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    trash[r-1][c-1] = 1

def bfs(r, c):
    cnt = 0

    dx = [-1, 1, 0, 0] #상 하 좌 우
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((r, c))

    if trash[r][c] == 0:
        return 0

    trash[r][c] = 0
    cnt += 1

    while queue:

        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < M:
                if trash[nx][ny]:
                    queue.append((nx, ny))
                    trash[nx][ny] = 0
                    cnt += 1
    return cnt

max_sector = 0

for i in range(N):
    for j in range(M):
        a = bfs(i,j)

        if max_sector < a:
            max_sector = a

print(max_sector)