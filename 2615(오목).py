omok = [list(map(int, input().split())) + [0]*4 for _ in range(19)]
omok = omok + [[0 for _ in range(23)] for _ in range(4)]

win = 0
position = []
for i in range(19):
    for j in range(19):
        #돌이 놓여져 있을 때
        if omok[i][j]:
            #우 검사
            for k in range(1, 5):
                if omok[i][j] != omok[i][j+k]:
                    break
            else:
                if omok[i][j] != omok[i][j+5] and omok[i][j] != omok[i][j-1]:
                    win = omok[i][j]
                    break
            #하 검사
            for k in range(1, 5):
                if omok[i][j] != omok[i+k][j]:
                    break
            else:
                if omok[i][j] != omok[i+5][j] and omok[i][j] != omok[i-1][j]:
                    win = omok[i][j]
                    break
            #5시방향
            for k in range(1, 5):
                if omok[i][j] != omok[i+k][j+k]:
                    break
            else:
                if omok[i][j] != omok[i+5][j+5] and omok[i][j] != omok[i-1][j-1]:
                    win = omok[i][j]
                    break
            #1시방향
            for k in range(1, 5):
                if omok[i][j] != omok[i-k][j+k]:
                    break
            else:
                if omok[i][j] != omok[i-5][j+5] and omok[i][j] != omok[i+1][j-1]:
                    win = omok[i][j]
                    break
    if win:
        position.append(i+1)
        position.append(j+1)
        break

print(win)
print(*position)