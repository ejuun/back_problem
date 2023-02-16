N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []

def back(start):
    if len(arr) == M:
        print(*arr)
    else:
        for i in range(start, N):
            if num[i] not in arr:
                arr.append(num[i])
                back(i)
                arr.pop()
back(0)