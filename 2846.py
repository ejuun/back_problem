N = int(input())
height_list = list(map(int,input().split())) 
diff_list = []
diff_sum = 0
for i in range(N-1):
    if height_list[i+1] -height_list[i] > 0 :
        diff_sum += height_list[i+1] -height_list[i]
        diff_list.append(diff_sum)
    else:
        diff_sum = 0
        diff_list.append(diff_sum)
print(max(diff_list))