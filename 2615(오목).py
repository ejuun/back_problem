omok = [list(map(int, input().split())) + [0]*4 for _ in range(23)]

win = 0
position = []
for i in range(19):
    for j in range(19):
        #돌이 놓여져 있을 때
        if omok[i][j]:
            #우 검사
            if (omok[i][j] == omok[i][j+k] for k in range(1,5)):
                if omok[i][j] != omok[i][j+5] and omok[i][j] != omok[i][j-1]:
                    win = omok[i][j]
                    position.append(i+1)
                    position.append(j+1)
                    break
            #하 검사
            elif (omok[i][j] == omok[i+k][j] for k in range(1, 5)):
                if omok[i][j] != omok[i+5][j] and omok[i][j] != omok[i-1][j]:
                    win = omok[i][j]
                    position.append(i+1)
                    position.append(j+1)
                    break
            #5시방향
            elif (omok[i][j] == omok[i+k][j+k] for k in range(1, 5)):
                if omok[i][j] != omok[i+5][j+5] and omok[i][j] != omok[i-1][j-1]:
                    win = omok[i][j]
                    position.append(i+1)
                    position.append(j+1)
                    break
            #1시방향
            elif (omok[i][j] == omok[i-k][j+k] for k in range(1, 5)):
                if omok[i][j] != omok[i-5][j+5] and omok[i][j] != omok[i+1][j-1]:
                    win = omok[i][j]
                    position.append(i+1)
                    position.append(j+1)
                    break
    if win:
        break

print(win)
print(*position)