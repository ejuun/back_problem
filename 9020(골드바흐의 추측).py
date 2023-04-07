def prime(N):
    arr = [0] * (N+1)
    ans = []
    for i in range(2, len(arr)):
        if not arr[i]:
            for j in range(i*2, N+1, i):
                arr[j] = 1

    for i in range(2, len(arr)):
        if not arr[i]:
            ans.append(i)

    return ans


for tc in range(int(input())):
    N = int(input())
    able = prime(N)

    min_diff = N
    a = b = N
    for i in able:
        for j in able:
            if i + j == N:
                if min_diff > abs(i-j):
                    min_diff = abs(i-j)
                    a = i
                    b = j

    print(a, b)
