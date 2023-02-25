N, M, L = map(int, input().split())

visited = [0] * (N+1)

cnt = 0

visited[1] = 1
i = 1
while M not in visited:
    if visited[i] % 2:
        if i + L > N:
            visited[i + L - N] += 1
            i = i + L - N
        else:
            visited[i+L] += 1
            i = i + L

    else:
        if i - L < 1:
            visited[N + i - L] += 1
            i = N + i - L
        else:
            visited[i - L] += 1
            i = i - L
    cnt += 1

print(cnt)

