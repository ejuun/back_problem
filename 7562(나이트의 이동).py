from collections import deque

for _ in range(int(input())):
    N = int(input())
    chess = [[0 for _ in range(N)] for _ in range(N)]
    s_r, s_c = map(int, input().split())
    e_r, e_c = map(int, input().split())

    # dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    # dc = [-2, -1, 1, 2, 2, 1, -1, -2]
    #
    # queue = deque()
    # queue.append((s_r, s_c))
    # chess[s_r][s_c] = 1
    #
    # while queue:
    #     r, c = queue.popleft()
    #
    #     for dir in range(8):
    #         nr = r + dr[dir]
    #         nc = c + dc[dir]
    #         if 0 <= nr < N and 0 <= nc < N:
    #             if not chess[nr][nc]:
    #                 queue.append((nr, nc))
    #                 chess[nr][nc] = chess[r][c] + 1
    #
    # print(chess[e_r][e_c]-1)