N = int(input())

i = 0
max_len = 0
ans_list = []

while i <= N:
    num = [N, i]

    while num[-1] >= 0:
        num.append(num[-2] - num[-1])

    if max_len < len(num):
        max_len = len(num) - 1
        ans_list = num[:len(num) - 1]

    i += 1

print(max_len)
print(*ans_list)