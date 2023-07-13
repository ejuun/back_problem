N, M = map(int, input().split())
dic = {}
for _ in range(N):
    site, pw = map(str, input().split())

    if site not in dic:
        dic[site] = pw

for _ in range(M):
    q = input()

    if q in dic:
        print(dic[q])