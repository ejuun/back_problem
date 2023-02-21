from collections import deque

N, M, K, X = map(int, input().split())
#N : 도시의 개수, M : 도로의 개수, K : 거리 정보, X : 출발 도시 번호
G = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    #단방향 그래프
    G[A].append(B)

queue = deque()
visited = [0] * (N+1)
#출발점으로부터 떨어진 거리를 기록하는 리스트
distance = [0] * (N+1)

queue.append(X)
visited[X] = 1

while queue:
    v = queue.popleft()

    for w in G[v]:
        if not visited[w]:
            queue.append(w)
            visited[w] = 1
            distance[w] = distance[v] + 1

#출발점으로 부터 거리가 K인 도시 출력하기
for i in range(len(distance)):
    if distance[i] == K:
        print(i)
else:
    if K not in distance:
        print(-1)