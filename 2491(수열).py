N = int(input())
num = list(map(int, input().split()))

result = 0

if N <= 2:
    result = N

else:
    up_list = []
    up_cnt = 1
    for i in range(N-1):
        if num[i+1] >= num[i]:
            up_cnt += 1
        else:
            up_list.append(up_cnt)
            up_cnt = 1
    else:
        up_list.append(up_cnt)

    down_list = []
    down_cnt = 1
    for i in range(N - 1):
        if num[i + 1] <= num[i]:
            down_cnt += 1
        else:
            down_list.append(down_cnt)
            down_cnt = 1
    else:
        down_list.append(down_cnt)

    if max(max(up_list), max(down_list)) < 3:
        result = 2
    else:
        result = max(max(up_list), max(down_list))

print(result)