from collections import deque
lst = [0] *1000001
N = int(input())
lst[N] = 1

queue = deque()
queue.append(N)

d = [3, 2]

while queue:
    n = queue.popleft()
    if n == 1:
        break

    for dir in range(2):
        if not(n % d[dir]):
            dn = n // d[dir]
            queue.append(dn)
            if not lst[dn]:
                lst[dn] = lst[n] + 1
    mn = n - 1
    if not lst[mn]:
        queue.append(mn)
        lst[mn] = lst[n] + 1

print(lst[1]-1)