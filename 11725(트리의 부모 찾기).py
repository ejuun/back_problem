from collections import deque

N = int(input())

G = [[] for _ in range(N+1)]
#부모노드 기록할 배열
P = [0] * (N + 1)

for _ in range(N-1):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

queue = deque()
#방문처리 할 배열
visited = [0] * (N+1)

queue.append(1)
visited[1] = 1

while queue:
    v = queue.popleft()

    for w in G[v]:
        if not visited[w]:
            queue.append(w)
            visited[w] = 1
            P[w] = v

for i in range(2, len(P)):
    print(P[i])