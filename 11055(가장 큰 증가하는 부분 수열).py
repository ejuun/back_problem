import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

dp[0] = A[0]
if N == 1:
    print(dp[0])
else:
    for i in range(1, N):
        val = 0
        for j in range(i-1, -1, -1):
            if A[j] < A[i] and val < dp[j]:
                val = dp[j]
            dp[i] = val + A[i]
    # print(dp)
    print(max(dp))
