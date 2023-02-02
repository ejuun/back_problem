N = int(input())
level_list = []
for i in range(N):
    level = int(input())
    level_list.append(level)

cnt = 0

for j in range(len(level_list)-1, 0, -1):
    if level_list[j] <= level_list[j-1]:
        cnt += abs(level_list[j] - level_list[j-1]-1)
        level_list[j-1] = level_list[j] - 1
print(cnt)