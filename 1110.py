N = int(input())
cyclenum =0
cnt = 0
while N != cyclenum:
    N_hap = 0
    for num in str(N):
        N_hap += int(num)
    cyclenum = int(str(N)[-1] + str(N_hap)[-1])
    cnt += 1
print(cnt)