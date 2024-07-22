N, M = map(int ,input().split())
road = [0 for _ in range(101)]
race = [0 for _ in range(101)]
road_km = 0
race_km = 0
for _ in range(N):
    dis, km = map(int ,input().split())

    for i in range(road_km, road_km+dis +1):
        road[i] = km

    road_km += dis

for _ in range(M):
    dis, km = map(int, input().split())

    for i in range(race_km, race_km+dis +1):
        race[i] = km

    race_km += dis

ans = 0
for i in range(101):
    if ans < race[i] - road[i]:
        ans = race[i] - road[i]
print(ans)