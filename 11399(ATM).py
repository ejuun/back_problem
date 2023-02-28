N = int(input())
num = sorted(list(map(int, input().split())))
total_ans = 0
ans = 0
for n in num:
    ans = ans + n
    total_ans += ans

print(total_ans)