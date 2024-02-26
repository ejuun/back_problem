import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
best = [[] for _ in range(12)]
exists = [0] * 12
ans = 0
for _ in range(N):
    p, w = map(int, input().split())
    heapq.heappush(best[p], -w)
    exists[p] = 1

for _ in range(K):
    for i in range(1, 12):
        if exists[i]:
            aug = -heapq.heappop(best[i])
            if aug == 1:
                break
            aug -= 1
            heapq.heappush(best[i], -aug)

for i in range(1,12):

    if exists[i]:
        ans += -heapq.heappop(best[i])
print(ans)