import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    C, K = map(int, input().split())
    if(K > 1):
        ans += C * K
    elif (K == 1):
        ans += C

print(ans)