import sys

def cal_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]

if N == 0:
    print(0)
else:
    lst.sort()
    num = cal_round(N * 0.15)
    div = N - 2 * num
    if num:
        lst = lst[num: -num]
    ans = cal_round(sum(lst) / div)
    print(ans)