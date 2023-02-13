# omok = [list(map(int, input().split())) for _ in range(19)]
#
# def check_black():
#     for i in range(19):
#         for j in range(19):
#             cnt = 0
#             #흑돌이 있을 때
#             if omok[i][j] == 1:
#                 #우 검사
#                 for k in range(5):
#                     if j+k <= 0 or j+k >= 19:
#                         cnt = 0
#                         break
#                     elif omok[i][j+k] == 1:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#                 #하 검사
#                 for k in range(5):
#                     if i + k <= 0 or i + k >= 19:
#                         cnt = 0
#                         break
#                     elif omok[i + k][j] == 1:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#                 #우하 검사
#                 for k in range(5):
#                     if i + k <= 0 or i + k >= 19 or j + k <= 0 or j + k >= 19:
#                         cnt = 0
#                         break
#                     elif omok[i + k][j + k] == 1:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#
#                 # 좌하 검사
#                 for k in range(5):
#                     if i + k <= 0 or i + k >= 19 or j - k <= 0:
#                         cnt = 0
#                         break
#                     elif omok[i + k][j - k] == 1:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#
#     return 0
#
# def check_white():
#     for i in range(19):
#         for j in range(19):
#             cnt = 0
#             #백돌이 있을 때
#             if omok[i][j] == 2:
#                 #우 검사
#                 for k in range(5):
#                     if j+k <= 0 or j+k >= 19:
#                         cnt = 0
#                         break
#                     elif omok[i][j+k] == 2:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#                 #하 검사
#                 for k in range(5):
#                     if i + k <= 0 or i + k >= 19:
#                         cnt = 0
#                         break
#                     elif omok[i + k][j] == 2:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#                 #우하 검사
#                 for k in range(5):
#                     if i + k <= 0 or i + k >= 19 or j + k <= 0 or j + k >= 19:
#                         cnt = 0
#                         break
#                     elif omok[i + k][j + k] == 2:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#
#                 # 좌하 검사
#                 for k in range(5):
#                     if i + k <= 0 or i + k >= 19 or j - k <= 0:
#                         cnt = 0
#                         break
#                     elif omok[i + k][j - k] == 2:
#                         cnt += 1
#                     else:
#                         cnt = 0
#                         break
#                 if cnt == 5:
#                     return (i+1, j+1)
#
#     return 0
#
# b = check_black()
# w = check_white()
# if b != 0 and w == 0:
#     print(1)
#     print(*b)
# elif b == 0 and w != 0:
#     print(2)
#     print(*w)
# else:
#     print(0)
omok = [list(map(int, input().split())) for _ in range(19)]

def check_black():
    for i in range(19):
        for j in range(19):
            cnt = 0
            #흑돌이 있을 때
            if omok[i][j] == 1:
                print(i,j)
                #우 검사
                for k in range(5):
                    if j+k < 0 or j+k >= 19:
                        cnt = 0
                        break
                    elif omok[i][j+k] == 1:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if j - 1 >= 0 and omok[i][j-1] == 1:
                        cnt = 0
                    else:
                        return (i+1, j+1)
                #하 검사
                for k in range(5):
                    print(cnt)
                    if i + k < 0 or i + k >= 19:
                        cnt = 0
                        break
                    elif omok[i + k][j] == 1:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if i - 1 >= 0 and omok[i-1][j] == 1:
                        cnt = 0
                    else:
                        return (i+1, j+1)
                #우하 검사
                for k in range(5):
                    if i + k < 0 or i + k >= 19 or j + k < 0 or j + k >= 19:
                        cnt = 0
                        break
                    elif omok[i + k][j + k] == 1:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if i - 1 >= 0 and j - 1 >= 0 and omok[i - 1][j - 1] == 1:
                        cnt = 0
                    else:
                        return (i + 1, j + 1)

                # 좌하 검사
                for k in range(5):

                    if i + k < 0 or i + k >= 19 or j - k < 0:
                        cnt = 0
                        break
                    elif omok[i + k][j - k] == 1:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                    print(cnt)
                if cnt == 5:
                    if i-1 >= 0 and j + 1 <= 19 and omok[i - 1][j + 1] == 1:
                        cnt = 0
                    else:
                        return (i+5, j-3)
    return 0

def check_white():
    for i in range(19):
        for j in range(19):
            cnt = 0
            #백돌이 있을 때
            if omok[i][j] == 2:
                #우 검사
                for k in range(5):
                    if j+k < 0 or j+k >= 19:
                        cnt = 0
                        break
                    elif omok[i][j+k] == 2:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if j - 1 >= 0 and omok[i][j - 1] == 1:
                        cnt = 0
                    else:
                        return (i + 1, j + 1)
                #하 검사
                for k in range(5):
                    if i + k < 0 or i + k >= 19:
                        cnt = 0
                        break
                    elif omok[i + k][j] == 2:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if i - 1 >= 0 and omok[i - 1][j] == 1:
                        cnt = 0
                    else:
                        return (i + 1, j + 1)
                #우하 검사
                for k in range(5):
                    if i + k < 0 or i + k >= 19 or j + k < 0 or j + k >= 19:
                        cnt = 0
                        break
                    elif omok[i + k][j + k] == 2:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if i - 1 >= 0 and j - 1 >= 0 and omok[i - 1][j - 1] == 1:
                        cnt = 0
                    else:
                        return (i + 1, j + 1)

                # 좌하 검사
                for k in range(5):
                    if i + k < 0 or i + k >= 19 or j - k < 0:
                        cnt = 0
                        break
                    elif omok[i + k][j - k] == 2:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    if i - 1 >= 0 and j + 1 <= 19 and omok[i - 1][j + 1] == 1:
                        cnt = 0
                    else:
                        return (i + 5, j - 3)
    return 0

b = check_black()
w = check_white()
if b != 0 and w == 0:
    print(1)
    print(*b)
elif b == 0 and w != 0:
    print(2)
    print(*w)
else:
    print(0)