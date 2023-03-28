N = int(input())
time = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda x:(x[1],x[0]))

k = 0
cnt = 1
if len(time) >= 2:
    for i in range(1, len(time)):
        if time[i][0] >= time[k][1]:
            cnt += 1
            k = i
print(cnt)