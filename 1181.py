N = int(input())
online_user = []
for i in range(N):
    age, name = map(str,input().split())
    online_user.append((age,name))

sort_user = sorted(online_user, key= lambda x : (int(x[0])))

for user in sort_user:
    print(user[0], user[1])