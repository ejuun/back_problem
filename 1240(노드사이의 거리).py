from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, r, w = map(int, input().split())
    G[s].append((r, w))
    G[r].append((s, w))

INF = 1e9
def find(start, end):
    queue = deque()
    queue.append(start)
    visited = [INF] * (N+1)
    visited[start] = 0

    while queue:
        x = queue.popleft()

        for end_p, weight in G[x]:
            if visited[end_p] > visited[x] + weight:
                visited[end_p] = visited[x] + weight
                queue.append(end_p)

    return visited[end]

for _ in range(M):
    start, end = map(int, input().split())
    print(find(start, end))