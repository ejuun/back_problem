N = int(input())
area_list = []
dirc_list = []
garo_list = []
sero_list = []
empty = 0

for i in range(6):
    direct, length = map(int, input().split())
    area_list.append((direct, length))
    dirc_list.append(direct)

    if direct == 1 or direct == 2:
        garo_list.append((length, direct))
    else:
        sero_list.append((length, direct))


#최대 가로 길이 구하기
max_garo = -1
for i in range(len(garo_list)):
    if max_garo < garo_list[i][0]:
        max_garo = garo_list[i][0]

#최대 세로길이 구하기
max_sero = -1
for i in range(len(sero_list)):
    if max_sero < sero_list[i][0]:
        max_sero = sero_list[i][0]

#최대 가로 * 최대 세로
total_area = max_garo * max_sero
ans_area = total_area - empty
ans = ans_area * N

print(ans)