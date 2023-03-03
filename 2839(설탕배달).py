from collections import deque

N = int(input())

sugar = [0] * 5001

dx = [5, 3]

sugar[3] = 1
sugar[5] = 1

queue = deque()
queue.append(5)
queue.append(3)

while queue:
    if sugar[N]:
        break

    x = queue.popleft()

    for dir in range(2):
        nx = x + dx[dir]
        if 0 <= nx < N+1:
            if not sugar[nx]:
                queue.append(nx)
                sugar[nx] = sugar[x] + 1

if not sugar[N]:
    print(-1)
else:
    print(sugar[N])