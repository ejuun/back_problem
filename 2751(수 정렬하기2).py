N = int(input())

plus_lst = [0] * 1000001
minus_lst =[0] * 1000001
for _ in range(N):
    n = int(input())
    if n >= 0:
        plus_lst[n] += 1
    else:
        minus_lst[-n] += 1

for i in range(len(minus_lst)-1, 0, -1):
    if minus_lst[i]:
        print(-i)

for i in range(len(plus_lst)):
    if plus_lst[i]:
        print(i)

