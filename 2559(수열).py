N, K = map(int, input().split())
num = list(map(int, input().split()))

max_temp = sum(num[:K])

temp = sum(num[:K])

for i in range(N-K):
    temp -= num[i]
    temp += num[K+i]

    if max_temp < temp:
        max_temp = temp

print(max_temp)
