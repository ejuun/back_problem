import sys
sys.setrecursionlimit(100000)
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    land = [[0 for _ in range(M)] for _ in range(N)]

    for k in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1
    cnt = 0

    def baechu(x,y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False

        if land[x][y] == 1:
            land[x][y] = 0
            baechu(x+1, y)
            baechu(x, y+1)
            baechu(x-1, y)
            baechu(x, y-1)
            return True
        return False

    for i in range(M):
        for j in range(N):
            if baechu(j,i) == True:
                cnt += 1
    print(cnt)
