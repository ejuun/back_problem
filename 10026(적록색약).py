from collections import deque
import copy
N = int(input())
#기존 리스트 받기
color = [list(map(str, input())) for _ in range(N)]
#빨강색과 녹색이 같은 리스트 생성
weakness = copy.deepcopy(color)
for i in range(N):
    for j in range(N):
        if weakness[i][j] == 'G':
            weakness[i][j] = 'R'
#color, weakness 방문처리 위한 행렬 생성
visited_c = [[0 for _ in range(N)] for _ in range(N)]
visited_w = [[0 for _ in range(N)] for _ in range(N)]

def bfs(graph, visited, r, c):

    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((r, c))
    #방문처리 == 1
    #방문한 적이 있다면
    if visited[r][c] == 1:
        return 0
    #시작점 방문처리
    visited[r][c] = 1

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < N:
                #0이면 (방문한 적이 없다면)
                if not visited[nx][ny]:
                    #두 포인트의 색이 같다면
                    if graph[nx][ny] == graph[x][y]:
                        queue.append((nx, ny))
                        #해당지점 방문처리
                        visited[nx][ny] = 1
    return 1
    #한 지점에 대해 같은 색을 모두 방문했다면 1반환

c = w = 0

for i in range(N):
    for j in range(N):
        if bfs(color,visited_c, i, j):
            c += 1
        if bfs(weakness,visited_w, i, j):
            w += 1
print(c, w)