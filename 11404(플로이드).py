N = int(input())
M = int(input())
INF = 10e9
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(N+1):
    for j in range(N+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, N):
    for j in range(1, N+1):
        print(graph[i][j], end=' ')
    print()

print(*graph[-1][1:])