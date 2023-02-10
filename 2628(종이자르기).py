w, h = map(int, input().split())

N = int(input())

sero = [0, w]
garo = [0, h]

for i in range(N):
    which, size = map(int, input().split())

    if which == 0:
        garo.append(size)
    else:
        sero.append(size)

garo.sort()
sero.sort()

max_garo = -1
for i in range(len(garo)-1):
    garo_diff = garo[i+1] - garo[i]
    if max_garo < garo_diff:
        max_garo = garo_diff

max_sero = -1
for i in range(len(sero)-1):
    sero_diff = sero[i+1] - sero[i]
    if max_sero < sero_diff:
        max_sero = sero_diff

print(max_garo * max_sero)
