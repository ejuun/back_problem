N = int(input())
N_list = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))

for M in M_list:
    if M in N_list:
        print(1)
    else:
        print(0)