from collections import deque

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# 공기 부분 -1로 바꾸기
air = deque()
air.append((0, 0))
arr[0][0] = -1

while air:
    x, y = air.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if not arr[nx][ny]:
                arr[nx][ny] = -1
                air.append((nx, ny))

# for line in arr:
#     print(*line)
# print('================================')

cnt = 0
last_cheese = 0

while 1:
    #시간 경과
    cnt += 1

    change_cheese = set()
    #공기와 만난 치즈 구하기
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        if arr[ni][nj] == -1:
                            change_cheese.add((i, j))
                            break

    #녹여질 치즈의 갯수
    last_cheese = len(change_cheese)

    #공기와 만난 치즈 녹이기
    for i, j in change_cheese:
        arr[i][j] = -1


    #구멍과 공기 접촉 여부 확인
    hole = deque()
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        if arr[ni][nj] == -1:
                            hole.append((i, j))
                            break

                while hole:

                    x, y = hole.popleft()

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < r and 0 <= ny < c:
                            if not arr[nx][ny]:
                                arr[nx][ny] = -1
                                hole.append((nx, ny))

    #남아있는 치즈 여부 확인
    save_cheese = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                save_cheese += 1
                break
        if save_cheese:
            break

    #남아 있는 치즈 없다면 break
    if not save_cheese:
        break


print(cnt)
print(last_cheese)