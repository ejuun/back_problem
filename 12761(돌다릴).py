from collections import deque
A, B, N, M = map(int, input().split())
visited = [0] * 100001

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()

    if x == M:
        break

    for move in [x-1, x+1, x-A, x+A, x-B, x+B, x*A, x*B]:
        nx = move
        if 0 <= nx < 100001:
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)
                if nx == M:
                    break
    if nx == M:
        break
print(visited[M])