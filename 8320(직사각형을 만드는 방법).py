N = int(input())
# ans = [0] * 10001
# for i in range(3, 10001):
#     if i % 2 == 0:
#         ans[i] = ans[i-1] + 2
#     else:
#         for j in range(2, 100):
#             if j * j == i:
#                 ans[i] = ans[i-1] + 2
#                 break
#         else:
#             ans[i] = ans[i-1] + 1
#
# print(ans[N])
cnt = 0
for i in range(1, int(N**0.5)+1):
    for j in range(i, N // i + 1):
        cnt += 1
print(cnt)