N = int(input())

five = 0

for i in range(1, 4):
    five += N // (5 ** i)

print(five)