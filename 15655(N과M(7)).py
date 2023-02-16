N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []

def back():
    if len(arr) == M:
        print(*arr)

    else:
        for i in range(N):
            arr.append(num[i])
            back()
            arr.pop()
back()