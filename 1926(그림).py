from collections import deque

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1] #상하좌우

def bfs(r, c):
    global picture
    cnt = 1
    queue.append((r, c))
    picture[r][c] = 0
    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if picture[nx][ny]:
                    queue.append((nx, ny))
                    picture[nx][ny] = 0
                    cnt += 1
    return cnt
# print(bfs(0,0))
# for line in picture:
#     print(*line)
# print(bfs(3,2))
max_size = 0
for i in range(n):
    for j in range(m):
        print(bfs(i,j))
        # if bfs(i,j) > 1:
        #     print(bfs(i,j))
        #     if max_size < bfs(i,j):
        #         max_size = bfs(i,j)
        #         print(max_size)
print(picture)

# found_list = []
# def dfs(x,y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#
#     if picture[x][y] == 1:
#         picture[x][y] = 0
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x-1, y)
#         dfs(x, y-1)
#         return True
#     return False
# #그림의 갯수 구하기
# cnt = 0
# for i in range(m):
#     for j in range(n):
#         if dfs(j,i) == True:
#             cnt += 1
# print(cnt)
