import heapq
INF = int(1e9)
V, E = map(int, input().split())# v : 정점의 개수, e : 간선의 개수
K = int(input())#시작 정점의 번호
graph = [[] for _ in range(V+1)] #정점의 개수 + 1개 만큼 그래프생성
#인덱스 번호 맞추기 위해
distance = [INF] * (V+1) #각 거리 표시 리스트도 그래프에 맞춰 생성

for _ in range(E):
    u, v, w = map(int, input().split()) # u => v, 가중치 w
    graph[u].append((v, w))

def dijk(K):
    q = []
    distance[K] = 0
    heapq.heappush(q, (0, K)) #heapq에 시작점이라 거리가 0이고 시작점의 노드 번호인 K를 push함
    while q:
        dist, now_locate = heapq.heappop(q) #현재 위치의 거리와 인덱스를 pop으로 꺼냄
        if distance[now_locate] < dist: #만약 now를 방문한 적이 있다면 / 지금 거리보다 지금 거리보다 원래 거리가 더 짧다면 패스
            continue
            #왜냐하면 지금 이 알고리즘 상 가장 짧은 곳을 먼저 탐색하는데 이전 길이가 더 크다면 이미 방문 했다는 뜻임
        for i in graph[now_locate]: #지금위치에서 다른 노드까지의 거리를 탐색
            #i[0]= 노드 번호, i[1] = 거리
            cost = dist + i[1] #지금까지의 거리와 다른 노드 사이의 거리를 더함
            if distance[i[0]] > cost: #원래 거리보다 지금 노드에서 가는게 더 빠르다면
                distance[i[0]] = cost #원래거리에 뒤집어 씌움
                heapq.heappush(q, (cost, i[0])) #그리고 그 거리와 다음 노드 위치를 저장

dijk(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])