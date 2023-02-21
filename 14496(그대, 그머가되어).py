from collections import deque
a, b = map(int, input().split())
N, M = map(int, input().split()) #N 문자의 수, M 문자쌍의 수

G = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

queue = deque()
queue.append(a)
visited[a] = 1
#치환 횟수 기록하는 행렬 생성
count = [0] * (N+1)
#출발점을 0으로 설정시
# a == b 인경우 치환횟수가 0인데 치환할 수 없는 경우도 0이므로
#구분해 주기 위해 시작점부터 1
#치환이 안된다면 0 -1 = -1, 나머지는 한번 더 더해진것이므로 -1

count[a] = 1
while queue:
    t = queue.popleft()

    for w in G[t]:
        if not visited[w]:
            queue.append(w)
            count[w] = count[t] + 1
            visited[w] = 1

print(count[b]-1)