import copy
import sys
N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

arr = []
combi_list = []

def back():
    global arr

    if len(arr) == M:
        a = copy.deepcopy(arr)
        if not a in combi_list:
            combi_list.append(a)

    else:
        for i in range(len(num)):
            arr.append(num[i])
            back()
            arr.pop()

back()
for line in combi_list:
    print(*line)

