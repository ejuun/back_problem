import sys
N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

arr = []
idx = []
combi_list = set()

def back(start):

    if len(arr) == M:
        if tuple(arr) not in combi_list:
            print(*arr)
            combi_list.add(tuple(arr))
            return
        else:
            return

    for i in range(start, N):
        # if i not in idx:
        #     idx.append(i)
            arr.append(num[i])
            back(i)
            arr.pop()
            # idx.pop()
back(0)