def div(a, b):
    if b == 1:
        return a % C

    quen = div(a, b // 2)

    if b // 2:
        return quen * quen * a % C
    else:
        return quen * quen % C

A, B, C = map(int, input().split())

print(div(A, B))
