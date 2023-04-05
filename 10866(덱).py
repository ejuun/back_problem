import sys
from collections import deque
N = int(sys.stdin.readline())
deque = deque()
data = [sys.stdin.readline().rstrip() for _ in range(N)]

for word in data:
    if word[:10] == 'push_front':
        deque.appendleft(word[11:])
    elif word[:9] == 'push_back':
        deque.append(word[10:])

    elif word[:9] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif word[:8] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)

    elif word[:4] == 'size':
        print(len(deque))

    elif word[:5] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif word[:5] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    else:
        if deque:
            print(deque[-1])
        else:
            print(-1)