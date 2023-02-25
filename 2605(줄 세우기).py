N = int(input())

line = []

num = list(map(int, input().split()))

cnt = 1
for i in range(len(num)):
    if num[i] == 0:
        line.append(cnt)
    else:
        line.insert(len(line)-num[i], cnt)

    cnt += 1

print(*line)