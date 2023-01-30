N = int(input())
num_list = [0] * 10000
for i in range(N):
    num = int(input())
    num_list[i] = num

s_num = sorted(num_list)

for i in s_num:
    if i != 0:
        print(i)