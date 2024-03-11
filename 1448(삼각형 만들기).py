N = int(input())
tri = []
for _ in range(N):
    tri.append(int(input()))
tri.sort()
ans = -1

while len(tri) >= 3:
    if tri[-1] >= tri[-2] + tri[-3]:
        tri.pop()
    else:
        ans = tri[-1] + tri[-2] + tri[-3]
        break

print(ans)
