# import sys
# input = sys.stdin.readline
#
# word = input()
# N = int(input())
# rings = []
# for _ in range(N):
#     ring = input().rstrip()
#     rings.append(ring+ring)
#
# ans = 0
# print(word)
# for check in rings:
#     if word in check:
#         ans += 1
# print(ans)

word = input()
N = int(input())
rings = []
for _ in range(N):
    ring = input()
    rings.append(ring+ring)
print(rings)
print(word)
ans = 0
for words in rings:
    if word in words:
        ans += 1
print(ans)