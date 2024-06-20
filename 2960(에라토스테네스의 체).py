N, K = map(int, input().split())
num = [True] * (N+1)
ans = []
idx = 0
for i in range(2, N+1):
    if num[i]:
        for j in range(i, N+1, i):
            if num[j]:
                num[j] = False
                ans.append(j)
                idx += 1
print(ans[K-1])