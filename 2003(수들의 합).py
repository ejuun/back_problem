N, M = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0
end = 0
interval = 0

for start in range(N):

    while interval < M and end < N:
        interval += seq[end]
        end += 1

    if interval == M :
        cnt += 1
    interval -= seq[start]

print(cnt)