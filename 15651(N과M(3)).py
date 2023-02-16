N, M = map(int, input().split())
arr = []

def back():
    if len(arr) == M:
        print(*arr)

    else:
        for i in range(1,N+1):
            arr.append(i)
            back()
            arr.pop()

back()