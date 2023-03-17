N = int(input())
num = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

m_list = [0] * 10000001
p_list = [0] * 10000001
for n in num:
    if n >= 0:
        p_list[n] += 1
    else:
        m_list[-n] += 1

for m in card:
    if m >= 0:
        print(p_list[m], end=' ')
    else:
        print(m_list[-m], end=' ')

# ans = [0] * M
#
# for i in range(len(num)):
#     if num[i] in card:
#         ans[card.index(num[i])] += 1
#
# print(*ans)