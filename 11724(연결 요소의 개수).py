N, M = map(int, input().split()) #N :노드 갯수, M : 간선의 갯수

G = [[] for _ in range(N+1)] #그래프 생성

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

#큐와 방문 기록을 위한 visited 생성
queue = []
visited = [False] * (N+1)

#모든 정점에 대해 시행할 bfs 함수 생성
def bfs(start):
    #큐에 시작점 삽입
    queue.append(start)
    #방문 기록 하기
    visited[start] = True

    while queue:
        t = queue.pop(0)

        for w in G[t]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
    #큐가 비었다면 visited 반환
    return visited
#함수 한번 실행하게 되면
#시작점에서 연결된 정점 방문기록이 남은 visited 반환 되어짐
cnt = 0
for i in range(1, len(visited)):
    if visited[i] == False:
        bfs(i)
        #print(visited)
        # 예제 1번 시행 결과 (1 - 2 - 5) , (3 - 4 - 6)
        # [False, True, True, False, False, True, False]
        # [False, True, True, True, True, True, True]
        cnt += 1

print(cnt)
