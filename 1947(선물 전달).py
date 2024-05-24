N = int(input())
dp = [0] * 1000001
dp[2] = 1
for i in range(3, N+1):
    dp[i] = ((i-1) * (dp[i-2] + dp[i-1])) % 1000000000

print(dp[N])