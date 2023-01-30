def rectangle(n):
    if n ==2:
        return 3
    elif n == 1:
        return 1
    else:
        return rectangle(n-1) + 2* rectangle(n-2)

n = int(input())
print(rectangle(n)%10007)