p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = p[1] + p[3]
p[5] = p[4]
for i in range(6, 101):
    p[i] = p[i-5] + p[i-1]

for _ in range(int(input())):
    N = int(input())
    print(p[N])
