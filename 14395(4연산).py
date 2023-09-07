from collections import deque

s, t = map(int, input().split())

visited = set()
queue = deque()
ans = ''

def find(s):
    global ans

    queue.append((s, ans))
    visited.add(s)

    while queue:
        x, sign = queue.popleft()

        if x > int(1e9):
            continue

        for cal in range(4):
            if cal == 0:
                new_x = x * x
                new_sign = sign + '*'
            elif cal == 1:
                new_x = x + x
                new_sign = sign + '+'
            elif cal == 2:
                new_x = x - x
                new_sign = sign + '-'
            elif cal == 3:
                if x:
                    new_x = x // x
                    new_sign = sign + '/'

            if new_x == t:
                ans = new_sign
                return

            if new_x not in visited:
                visited.add(new_x)
                queue.append((new_x, new_sign))


if s == t:
    print(0)

else:
    find(s)

    if ans == '':
        print(-1)
    else:
        print(ans)