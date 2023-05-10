from heapq import heappush, heappop

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

N, M = map(int, input().split())
p = [i for i in range(N + 1)]
G = []
for _ in range(M):
    A, B, C = map(int, input().split())
    G.append((A, B, C))
G.sort(key=lambda x:x[2])
    # heappush(G, (C, A, B))


cnt = ans = max_cost = 0

for u, v, cost in G:
    if find_set(u) != find_set(v):
        cnt += 1
        ans += cost
        union(u, v)
        max_cost = cost
        if cnt == N:
            break

print(ans-max_cost)