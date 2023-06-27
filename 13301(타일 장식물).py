n = int(input())

dp = [0] * 82

dp[1] = 1
dp[2] = 1

for i in range(3, 82):
    dp[i] = dp[i-1] + dp[i-2]

ans = 2 * (dp[n+1] + dp[n])
print(ans)