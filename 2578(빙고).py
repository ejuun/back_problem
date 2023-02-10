import copy
bingo = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]

zero = 0
#ans 각각의 원소에 대해
for i in range(5):
    for j in range(5):
        #bingo 각각의 원소를 비교
        for k in range(5):
            for l in range(5):
                #만약 같으면
                if bingo[k][l] == ans[i][j]:
                    #0처리
                    bingo[k][l] = 0
                    zero += 1
        #bg = 빙고 된 줄 수
        bg = 0
        dia = []
        re_dia = []
        #딥카피로 밑에 전치행렬 만들고 초기화
        sero = copy.deepcopy(bingo)
        #각 세로, 가로, 대각 라인 검사
        for a in range(5):
            #가로 검사
            if bingo[a] == [0, 0, 0, 0, 0]:
                bg += 1
            # 세로 검사
            for b in range(5):
                if a < b:
                    sero[a][b], sero[b][a] = sero[b][a], sero[a][b]
            if sero[a] == [0, 0, 0, 0, 0]:
                bg += 1
            #대각 검사
            dia.append(bingo[a][a])
            re_dia.append((bingo[4-a][a]))
        if dia == [0, 0, 0, 0, 0]:
            bg += 1
        if re_dia == [0, 0, 0, 0, 0]:
            bg += 1

        if bg >= 3:
            break
    if bg >= 3:
        break
print(zero)