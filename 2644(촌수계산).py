from collections import deque

n = int(input()) #전체 사람의 수
me, you = map(int, input().split()) #계산 해야 될 사람들
m = int(input()) #관계의 개수

G = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

queue = deque()
visited = [0] * (n+1)
#촌수 파악 하기 위한 리스트 생성
relation = [0] * (n+1)
#시작점(me) 삽입
queue.append(me)
visited[me] = 1

while queue:
    v = queue.popleft()

    for w in G[v]:
        if not visited[w]:
            queue.append(w)
            visited[w] = 1
            relation[w] = relation[v] + 1

if not relation[you]:
    relation[you] = -1
print(relation[you])
