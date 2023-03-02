N, K = map(int, input().split())
room = dict()
for _ in range(N):
    gender, grade = map(int, input().split())

    if (gender, grade) in room:
        room[(gender, grade)] += 1
    else:
        room[(gender, grade)] = 1

cnt = 0

for value in room.values():
    if value % K == 0:
        cnt += (value // K)
    else:
        cnt += ((value // K) + 1)


print(cnt)