C, R = map(int, input().split())
target = int(input())

seat = [[0 for _ in range(C)] for _ in range(R)]

r, c = R-1, 0
n = 1
i = 0

dx = [-1, 0, 1, 0] #상 우 하 좌
dy = [0, 1, 0, -1]

while True:
    seat[r][c] = n

    if n == C * R:
        break

    r += dx[i]
    c += dy[i]
    n += 1

    #범위 벗어 났을 때
    if r >= R or r < 0 or c >= C or c < 0 or seat[r][c] != 0:
        r -= dx[i]
        c -= dy[i]
        n -= 1

        i += 1
        i = i % 4

        r += dx[i]
        c += dy[i]
        n += 1

if target > C * R:
    print(0)
else:
    for i in range(R):
        for j in range(C):
            if seat[i][j] == target:
                print(j + 1, R - i)
                break

