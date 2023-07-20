N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(1):
    for j in range(3):
        dp[i][j] = arr[i][j]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + arr[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][j]

print(min(dp[N-1]))