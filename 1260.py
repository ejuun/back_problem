from collections import deque

N, M, start = map(int, input().split())

#방문 확인 리스트 생성
visited = [False] * (N+1) #인덱스 맞춰주기 위해 n개 보다 1개 더 설정
arr = [[] for _ in range(N+1)] #지나가는 경로 넣기 위한 빈 리스트생성
graph = [[]] #graph 문제 중 작은 값부터 방문해야된다는 조건 맞추기 위해 나중 arr sort값 넣기
for i in range(M):
    a, b = list(map(int, input().split()))
    arr[a].append(b)
    arr[b].append(a) #양 방향이기에 서로 이어진 곳 추가
for i in range(1, N+1):
    graph.append((sorted(arr[i]))) #문제 조건 맞추기 위한 작업

def dfs(graph, visited, start): #깊이 우선 탐색
    visited[start] = True #처음 출발점 True로 변환
    print(f'{start}', end=' ')
    for i in graph[start]: #출발점에서 이어져있는 길들
        if not visited[i]: #만약 방문하지 않았다면
            dfs(graph, visited, i) #해당장소를 시작점으로 다시 밑으로 진행

dfs(graph, visited, start)
print('', end ='\n')

visited = [False] * (N+1) #dfs 끝나서 다 True 됐기에 bfs 사용을 위해 초기화

def bfs(graph, visited, start): #deque 활용
    visited[start] = True #방문점 (출발점) True 변환
    queue = deque([start])     #deque 사용
    while queue: #방문이 다 끝날때까지
        v = queue.popleft() #방문한것 왼쪽부터 삭제
        print(f'{v}', end= ' ')
        for i in graph[v]: #방문완료된 v에서 갈수 있는 길들
            if not visited[i]: #방문하지 않은곳
                queue.append(i) #deque에 추가
                visited[i] = True #deque 추가하고 방문도 했으니 True로 변환
bfs(graph, visited, start)