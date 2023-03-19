N, M = map(int, input().split())
dic = dict()

for _ in range(N):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

for _ in range(M):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

d = sorted(dic.items())

total = 0
for name, cnt in dic.items():
    if cnt >= 2:
        total += 1
print(total)

for name, cnt in d:
    if cnt >= 2:
        print(name)