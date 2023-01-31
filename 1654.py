N, K = map(int,input().split())
line_list = []
for i in range(N):
    line = int(input())
    line_list.append(line)

min_line = 1
max_line = max(line_list)
result = 0
while min_line <= max_line:

    count_line = 0
    mid_line = (max_line + min_line) // 2

    for line in line_list:
        count_line += line//mid_line

    if count_line < K:
        max_line = mid_line -1    
    else:
        min_line = mid_line +1
        result = mid_line
print(result)

