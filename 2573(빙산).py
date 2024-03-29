from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def link(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

year = 0
while 1:
    year += 1

    # 녹는 면 구하기
    melting = set()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                melt = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 0:
                            melt += 1
                melting.add((i, j, melt))
    # 녹이기
    for i, j, melt in melting:
        if arr[i][j] - melt < 0:
            arr[i][j] = 0
        else:
            arr[i][j] -= melt

    # 나뉘는 부분 확인
    visited = [[0 for _ in range(M)] for _ in range(N)]
    div = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                link(i, j)
                div += 1
        #두 군데 이상이면 break
        if div >= 2:
            break
    #다 녹을때까지 분리되지 않았을 때
    if div == 0:
        year = 0
        break
    #두 군데 이상일 때
    elif div >= 2:
        break

print(year)
