import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N):
    for j in range(i+arr[i][0], N+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
print(dp[-1])

# for i in range(1, len(arr)):
#     if arr[i][0] + i -1 <= N:
#         if dp[arr[i][0] + i - 1]:
#             dp[arr[i][0] + i - 1] = max(dp[arr[i][0] + i - 1], dp[i] + arr[i][1])
#         else:
#             dp[arr[i][0] + i - 1] = dp[i] + arr[i][1]
#
# print(dp)