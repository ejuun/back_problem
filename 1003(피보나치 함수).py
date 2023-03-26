fibo = [[] for _ in range(41)]
fibo[0] = [1, 0]
fibo[1] = [0, 1]
# fibo[2] = (fibo[0][0]+fibo[1][0], fibo[0][1]+fibo[1][1])
# fibo[3] = (fibo[1][0]+fibo[2][0], fibo[1][1]+fibo[2][1])

for i in range(2, 41):
    fibo[i] = (fibo[i-2][0]+fibo[i-1][0], fibo[i-2][1]+fibo[i-1][1])

for _ in range(int(input())):
    n = int(input())
    print(*fibo[n])
