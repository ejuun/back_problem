small = []
for _ in range(9):
    height = int(input())
    small.append(height)

combi = []

def back(start):
    global small

    if len(combi) > 7 or sum(combi) > 100:
        return

    if len(combi) == 7 and sum(combi) == 100:
        combi.sort()
        for h in combi:
            print(h)
        return

    else:
        for i in range(start, len(small)):
            if small[i] not in combi:
                combi.append(small[i])
                back(i)
                # 길이가 7이면서 합이 100인것 중 가장 첫번째것만 나오도록 조건 설정
                # 이 조건을 넣지 않는다면 길이가 7이면서 합이 100을 만족하는 모든 조합 출력
                if len(combi) == 7 and sum(combi) == 100:
                    return
                combi.pop()

back(0)
# height_sum = sum(small)
#
# for i in range(9):
#     for j in range(i+1, 9):
#         if height_sum - (small[i]+ small[j]) == 100:
#             small.pop(j)
#             small.pop(i)
#             break
#     if len(small) == 7:
#         break
#
# small.sort()
# for s in small:
#     print(s)