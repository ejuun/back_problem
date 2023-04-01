N, K = map(int, input().split())

coin = [0] * (N+1)

cnt = 0

for i in range(1, N+1):
    coin[i] = int(input())

for money in coin[::-1]:
    if K >= money:
        cnt += K // money
        K = K - money * (K//money)


    if K == 0:
        break
print(cnt)