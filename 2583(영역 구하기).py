from collections import deque
M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    sr, sc, er, ec = map(int, input().split())

    a = M - sc #컴퓨터 행렬에 맞춘 시작 x좌표
    b = sr #시작 y 좌표
    c = M - ec #끝 x좌표
    d = er #끝 y 좌표

    for i in range(c, a):
        for j in range(b, d):
            paper[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #상 하 좌 우

def bfs(r,c):
    queue = deque()
    queue.append((r, c))
    cnt = 1
    paper[r][c] = 1

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < M and 0 <= ny < N:
                if not paper[nx][ny]:
                    queue.append((nx, ny))
                    paper[nx][ny] = 1
                    cnt += 1
    return cnt

result = []
total = 0
for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            a = bfs(i, j)
            result.append(a)
            total += 1
result.sort()

print(total)
print(*result)



