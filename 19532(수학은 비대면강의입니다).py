import math
a, b, c, d, e, f = map(int, input().split())

check = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            check = True
            print(x, y)
            break
    if check:
        break