from collections import deque

N, M, R = map(int, input().split())

visited = [0] * (N+1)
G = [[] for _ in range(N+1)]
new_G = [[]]
visited_sort = [0] * (N+1) #방문 순서 기록하는 행렬

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, N+1):
    new_G.append((sorted(G[i], reverse=True)))

queue = deque()

queue.append(R)
visited[R] = 1

i = 1
visited_sort[R] = i

while queue:
    t = queue.popleft()

    for w in new_G[t]:
        if not visited[w]:
            queue.append(w)
            visited[w] = 1
            i += 1
            visited_sort[w] = i

for i in range(1, N+1):
    print(visited_sort[i])