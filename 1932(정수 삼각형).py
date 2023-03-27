n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    tri[i+1][0] += tri[i][0]
    tri[i+1][-1] += tri[i][-1]

if n == 1:
    print(*tri[0])
elif n == 2:
    print(max(tri[1]))
else:
    for i in range(2, n):
        for j in range(1, i):
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

    print(max(tri[n-1]))