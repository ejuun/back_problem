record = [0]
N, M = map(int, input().split())
score = list(map(int, input().split()))

sum = 0
num = 100001

for i in range(M):
    tep = list(input().split())
    cnt = 0
    for j in range(1, N+1):
        if tep[j] =='O':
            cnt += int(score[j-1])

    if sum < cnt:
        sum = cnt
        num = int(tep[0])
    elif sum == cnt:
        num = min(num, int(tep[0]))

print(num, sum)

# total = [0 for _ in range(M)]
# idx = [0 for _ in range(M)]
# for id in range(M):
#     num, *ox = map(str, input().split())
#     idx[id] = num
#     for i in range(N):
#         if ox[i] == 'O':
#             total[id] += score[i]
# ans = []
# for i in range(M):
#     ans.append((idx[i], total[i]))
# ans.sort(key=lambda x: (-x[1], x[0]))
# print(*ans[0])