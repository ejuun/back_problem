# n, m = map(int, input().split())
#
# dp = [0] * 101
# dp[0] = 1
# dp[1] = 1
#
# for i in range(2, 101):
#     dp[i] = i * dp[i-1]
#
# ans = dp[n] // (dp[m] * dp[n-m])
#
# print(ans)

def fac(k):
    if k == 1 or k == 0:
        return 1
    else:
        return k * fac(k-1)

n, m = map(int, input().split())

ans = fac(n) // (fac(m) * fac(n-m))

print(ans)