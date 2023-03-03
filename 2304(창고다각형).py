N = int(input())

p = []
for _ in range(N):
    dot, h = map(int, input().split())
    p.append((dot, h))
p.sort()

#가장 높은 위치 찾기
max_height = 0
for i in range(len(p)):
    if max_height < p[i][1]:
        max_height = p[i][1]

area = 0

if p[0][1] == max_height:
    s = 0
    area += max_height

    while s != len(p)-1:
        m_h = 0
        which = 0
        for i in range(s+1, len(p)):
            if m_h <= p[i][1]:
                m_h = p[i][1]
                which = i
        area += ((p[which][0] - p[s][0]) * m_h)
        s = which

elif p[len(p)-1][1] == max_height:

    i = 0
    j = 1
    for _ in range(0, len(p)-1):
        if i == len(p)-1:
            break

        if p[i][1] >= p[j][1]:
            pass
        else:
            area += ((p[j][0]-p[i][0]) * p[i][1])
            i = j
        j += 1
    area += max_height

else:
    i = 0
    j = 1
    for _ in range(0, len(p)-1):
        if p[i][1] == max_height:
            break
        if p[i][1] >= p[j][1]:
            pass
        else:
            area += ((p[j][0]-p[i][0]) * p[i][1])
            i = j
        j += 1

    area += max_height

    while i != len(p)-1:
        m_h = 0
        which = 0
        for k in range(i+1, len(p)):
            if m_h <= p[k][1]:
                m_h = p[k][1]
                which = k
        area += ((p[which][0]- p[i][0]) * m_h)
        i = which

print(area)