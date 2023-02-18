def back(start):
    if len(able) > 6:
        return

    if len(able) == 6:
        print(*able)
        return

    else:
        for i in range(start, len(num)):
            if num[i] not in able:
                able.append(num[i])
                back(i)
                able.pop()

while True:
    N, *num = map(int, input().split())

    if N == 0:
        break
    able = []
    back(0)
    print()