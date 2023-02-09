import sys
sys.setrecursionlimit(100000)

while True:
    w, h = map(int, input().split()) #w: 너비, h: 높이
    if w == 0 and h == 0:
        break
    area = [list(map(int, input().split())) for _ in range(h)]

    def land(x, y): #x : 가로축 이동 , y: 세로축이동
        if x < 0 or x >= w or y < 0 or y >= h:
            return

        if area[y][x] == 1:
            area[y][x] = 0
            land(x+1, y)
            land(x, y+1)
            land(x-1, y)
            land(x, y-1)
            land(x + 1, y + 1)
            land(x + 1, y - 1)
            land(x - 1, y + 1)
            land(x - 1, y - 1)
            return True
        return

    cnt = 0
    for i in range(h):
        for j in range(w):
            if land(j, i) == 1:
                cnt += 1
    print(cnt)
