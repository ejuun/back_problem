from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            r, c = i, j
            break

day = 0

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1] #상하좌우

spread = [(r, c)]

# def bfs():
#     global spread
#
#     queue = deque()
#
#     if not spread:
#         return 0
#     else:
#         for sp in spread:
#             queue.append(sp)
#
#     spread.clear()
#
#     while queue:
#         x, y = queue.popleft()
#
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if not tomato[nx][ny]:
#                     spread.append((nx, ny))
#                     tomato[nx][ny] == 1
#     return 1

while spread:

    queue = deque()

    for sp in spread:
        queue.append(sp)

    spread.clear()

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if not tomato[nx][ny]:
                    spread.append((nx, ny))
                    tomato[nx][ny] == 1
    day += 1

print(day)


