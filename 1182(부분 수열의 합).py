def recur(idx, hap):
    global ans

    if idx >= N:
        return

    hap += arr[idx]

    if hap == S:
        ans += 1

    recur(idx+1, hap)
    recur(idx+1, hap-arr[idx])

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

recur(0, 0)
print(ans)
