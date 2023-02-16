n, m, r = map(int, input().split())
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

item = list(map(int, input().split()))
max_list = []

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n+1):
    graph[i][i] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# for i in range(n+1):
#     for j in range(n+1):
#         if graph[i][j] == INF:
#             graph[i][j] = 0

for i in range(1, n+1):
    get_item = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            get_item += item[j-1]
        max_list.append(get_item)

print(max(max_list))