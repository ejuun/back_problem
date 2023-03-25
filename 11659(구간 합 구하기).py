import  sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

hap = [0]
for i in range(N):
    hap.append(hap[i] + num[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(hap[j] - hap[i-1])