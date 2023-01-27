N, X = map(int,input().split())
num = list(map(int,input().split()))


for n in num:
    if X > n:
        print(n,end=' ')