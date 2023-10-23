str = input()
cnt = 0
for i in range(len(str)-1):
    if str[i] != str[i+1]:
       cnt += 1

if cnt % 2 :
    cnt += 1

ans = cnt // 2
print(ans)