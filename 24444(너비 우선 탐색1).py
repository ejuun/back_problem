from collections import deque

N, M, start = map(int, input().split())

visited = [False] * (N+1) #방문 지점 N+1개만큼 생성
graph = [[] for _ in range(N+1)] #정점 N개에 대해 각 지점마다 지나가는 길 입력을 위한 배열 생성
sort_graph = [[]]
node = [0] * (N +1)

for i in range(M): #M개의 간선 입력
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s) #무방향

for i in range(1, N+1):
    sort_graph.append((sorted(graph[i])))

def bfs(graph, visited, start):
    num = 1
    node[start] = 1

    visited[start] = True
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for i in graph[u]:
            if not visited[i]:
                queue.append(i)
                num += 1
                node[i] = num
                visited[i] = True

bfs(sort_graph, visited, start)
for i in range(1, N+1):
    print(node[i])