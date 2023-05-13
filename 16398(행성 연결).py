def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

p = [i for i in range(N + 1)]
G = []

for i in range(N):
    for j in range(i + 1, N):
        G.append((i + 1, j + 1, lst[i][j]))
G.sort(key=lambda x: x[2])

cost = len = 0

for p1, p2, c in G:
    if find_set(p1) != find_set(p2):
        len += 1
        cost += c
        union(p1, p2)
        if len == N:
            break

print(cost)