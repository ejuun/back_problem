N = int(input())
arr = list(map(int, input().split()))
set_arr = list(set(arr))
sort_arr = sorted(set_arr)

dic = {sort_arr[i]: i for i in range(len(sort_arr))}

ans = [0] * N
for i in range(len(arr)):
    if arr[i] in dic:
        ans[i] = dic[arr[i]]

print(*ans)