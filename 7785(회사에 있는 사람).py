import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    name, work = map(str, input().split())
    if work == "enter":
        lst.append(name)
    else:
        lst.remove(name)
lst.sort(reverse=True)
for name in lst:
    print(name)