N = int(input())
candidate = int(input())
can_num = list(map(int, input().split()))
#생각한 것 : 길이가N인 리스트 생성해서 후보자 오른쪽에서 왼쪽으로 저장
#          리스트가 다 채워졌으면 추천 수 가장 작은 것 가장 왼쪽으로보내고 삭제
#          후 오른쪽에 새로운 후보 넣기
    #후보자 번호, 카운트 횟수
can_list = [[0, 0] for _ in range(N)]
c_list = [0 for _ in range(N)] #후보자 번호만 따로 저장 하는 리스트
for i in can_num:
    #후보자 번호 맞춰주기 위해 동기화
    for n in range(N):
        c_list[n] = can_list[n][0]
    #후보자 번호가 리스트 내 없을떄
    if i not in c_list:
        #1. 리스트가 꽉 찼을때
        if 0 not in c_list:
            #만약 가장 적은 추천을 받은 후보자가 제일 게시된지 오래됐을 때 그대로 진행
            if min(can_list, key= lambda x: x[1]) == can_list[0]:
                for j in range(N-1):
                    can_list[j] = can_list[j+1]
                can_list[-1] = [i, 1]
            #가장 적은 추천을 받은 후보자보다 게시된지 오래된 후보자가 있을때 => 가장 추천적은 후보자 맨 앞으로 옮기기
            else:
                min_can = min(can_list, key=lambda x: x[1])
                can_list.remove(min_can)
                can_list.insert(0, min_can)

                for j in range(N - 1):
                    can_list[j] = can_list[j + 1]
                can_list[-1] = [i, 1]
        #2. 꽉 안찼을 경우 맨뒤에서부터 집어넣기
        else:
            for j in range(N - 1):
                can_list[j] = can_list[j + 1]
            can_list[-1] = [i, 1]
    #후보자 번호가 리스트 내 있을 때
    else:
        #후보자가 있는 곳에 cnt += 1
        for j in range(len(can_list)):
            if i == can_list[j][0]:
                can_list[j][1] += 1
#출력형식 맞춰주기 : 학생 번호 오름차순 출력
final = sorted(can_list, key=lambda x: x[0])
#만약 0이 남아 있을 경우 0제거
while True:
    if [0, 0] in final:
        final.remove([0, 0])
    else:
        break

for i in range(len(final)-1):
    print(final[i][0], end=' ')
print(final[-1][0])