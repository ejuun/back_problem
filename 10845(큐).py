import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
data = [sys.stdin.readline().rstrip() for _ in range(N)]

for word in data:
    if word[:4] == 'push':
        queue.append(word[5:])

    elif word[:3] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif word[:4] == 'size':
        print(len(queue))

    elif word[:5] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif word[:5] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)