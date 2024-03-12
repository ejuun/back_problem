N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

blue = white = 0

def div(n, row, col):
    global blue, white

    check = p[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != p[i][j]:
                check = -1
                break
        if check == -1:
            break
    if check == -1:
        div(n//2, row, col)
        div(n//2, row, col + n//2)
        div(n//2, row + n//2, col)
        div(n//2, row + n//2, col + n//2)
    else:
        if check == 1:
            blue += 1
        else:
            white += 1

div(N, 0, 0)
print(white)
print(blue)