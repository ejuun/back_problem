# def man(switch_list, n):
#     i = 1
#     while i * n <= len(switch_list):
#         if switch_list[i * n - 1] == 1:
#             switch_list[i * n - 1] = 0
#         else:
#             switch_list[i * n - 1] = 1
#         i += 1
#     return switch_list
#
# def woman(switch_list, n):
#     if len(switch_list) == 1:
#         if switch_list[n - 1] == 1:
#             switch_list[n - 1] = 0
#         else:
#             switch_list[n - 1] = 1
#         return switch_list
#     elif len(switch_list) == 2:
#         if switch_list[n - 1] == 1:
#             switch_list[n - 1] = 0
#         else:
#             switch_list[n - 1] = 1
#         return switch_list
#     else:
#         if switch_list[n - 2] != switch_list[n] or n - 1 == 0 or n == len(switch_list):
#             if switch_list[n - 1] == 1:
#                 switch_list[n - 1] = 0
#             else:
#                 switch_list[n - 1] = 1
#
#             return switch_list
#
#         else:
#             if switch_list[(n - 1)] == 1:
#                 switch_list[(n - 1)] = 0
#             else:
#                 switch_list[(n - 1)] = 1
#
#             i = 1
#             while switch_list[(n - 1) - i] == switch_list[(n - 1) + i]:
#
#                 if switch_list[(n - 1) - i] == 1:
#                     switch_list[(n - 1) - i] = 0
#                     switch_list[(n - 1) + i] = 0
#                 else:
#                     switch_list[(n - 1) - i] = 1
#                     switch_list[(n - 1) + i] = 1
#                 if n - i - 1 == 0 or n - 1 + i == len(switch_list) - 1:
#                     break
#                 i += 1
#             return switch_list
#
# switch = int(input())
# switch_list = list(map(int, input().split()))
# student_number = int(input())
#
# for i in range(student_number):
#     gender, n = map(int, input().split())
#
#     if gender == 1:
#         man(switch_list, n)
#     if gender == 2:
#         woman(switch_list, n)
#
# for i in range(0, len(switch_list), 20):
#     try:
#         print(*switch_list[i:i+20])
#     except Exception:
#         print(*switch_list[i:])
def woman(cnt):
    while True:
        # 겹치는게 없거나 끝에 위치한 경우 본인만 전환
        if (cnt-1) == 0 or (cnt-1) == len(switch)-1 or switch[(cnt - 1) - 1] != switch[(cnt-1) + 1]:
            if switch[(cnt - 1)] == 0:
                switch[(cnt - 1)] = 1
            else:
                switch[(cnt - 1)] = 0
            break
        # cnt - n == cnt + 1
        else:
            # 기준 왼,오로 같은게 있을 경우
            # 우선 자기 자신 변환
            if switch[(cnt - 1)] == 0:
                switch[(cnt - 1)] = 1
            else:
                switch[(cnt - 1)] = 0
            n = 1
            while True:
                if (cnt-1)-n < 0 or (cnt-1) + n >= len(switch) or switch[(cnt-1)-n] != switch[(cnt-1)+n]:
                    return switch
                if switch[(cnt - 1) - n] == 0:
                    switch[(cnt - 1) - n] = 1
                    switch[(cnt - 1) + n] = 1
                else:
                    switch[(cnt - 1) - n] = 0
                    switch[(cnt - 1) + n] = 0
                n += 1
    return switch

def man(cnt):
    n = 1
    while True:
        if cnt * n > len(switch):
            break
        if switch[cnt * n - 1] == 0:
            switch[cnt * n - 1] = 1
        else:
            switch[cnt * n - 1] = 0

        n += 1
    return switch

N = int(input())
switch = list(map(int, input().split()))
student = int(input())

for i in range(student):
    gender, cnt = map(int, input().split())

    if gender == 1:
        man(cnt)
    else:
        woman(cnt)

for i in range(0, len(switch), 20):
    try:
        print(*switch[i:i+20])
    except Exception:
        print(*switch[i:])

