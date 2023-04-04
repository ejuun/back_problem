from collections import deque

def bfs(q):
    queue.append(q)

    visitied[q] = 1

    while queue:
        x = queue.popleft()

        for dot in G[x]:
            if not visitied[dot]:
                visitied[dot] = visitied[x] + 1
                queue.append(dot)

    return max(visitied)-1

N = int(input())
G = [[] for _ in range(N+1)]
while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    G[u].append(v)
    G[v].append(u)

queue = deque()

ans = [0] * N

for i in range(1, N+1):
    visitied = [0] * (N+1)
    ans[i-1] = bfs(i)

score = min(ans)
cnt = ans.count(min(ans))

print(score, cnt)
for i in range(len(ans)):
    if ans[i] == score:
        print(i+1, end=' ')