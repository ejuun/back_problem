from collections import deque

V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

start = 1

visited = [False] * (V+1)
visited[start] = True
cnt = 0

queue = deque()
queue.append(start)
while queue:
    t = queue.popleft()

    for w in G[t]:
        if not visited[w]:
            queue.append(w)
            visited[w] = True
            cnt += 1

print(cnt)