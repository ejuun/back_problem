m = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    sr, sc, er, ec = map(int, input().split())

    re_sr = 100 - sc
    re_sc = sr
    re_er = 100 - ec
    re_ec = er

    for i in range(re_er, re_sr):
        for j in range(re_sc, re_ec):
            m[i][j] = 1

for line in m:
    print(*line)

cnt = 0
for line in m:
    cnt += line.count(1)

print(cnt)