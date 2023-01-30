N, M =map(int,input().split())
num = list(map(int,input().split()))
sum_list = []
for i in range(len(num)-2):
    for j in range(i+1,len(num)-1):
        for k in range(j+1,len(num)):
            sum_list.append(num[i] +num[j] + num[k])

s_list = sorted(sum_list)
for i in range(len(s_list)):
    if s_list[-1] <= M:
        print(s_list[-1])
        break
    
    elif s_list[i] > M:
            print(s_list[i-1])
            break
