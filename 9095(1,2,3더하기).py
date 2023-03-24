num = [1, 2, 3]
arr = []

def hap():
    global cnt
    if sum(arr) == n:
        cnt += 1
        return
    elif sum(arr) > n:
        return

    for i in range(len(num)):
        arr.append(num[i])
        hap()
        arr.pop()

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    hap()
    print(cnt)