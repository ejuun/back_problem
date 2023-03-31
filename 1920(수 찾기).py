N = int(input())
n = list(map(int, input().split()))
dic = dict()
for num in n:
    dic[num] = 1

M = int(input())
m = list(map(int, input().split()))

for num in m:
    if num in dic:
        print(1)
    else:
        print(0)