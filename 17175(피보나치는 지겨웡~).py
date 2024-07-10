n = int(input())
dp = [1] * 51
for i in range(2, 51):
    dp[i] = (dp[i-2] + dp[i-1] + 1) % 1000000007
print(dp[n])