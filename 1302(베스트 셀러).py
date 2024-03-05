import sys
input = sys.stdin.readline
N = int(input())
books = dict()
for _ in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_val = 0
for key, value in books.items():
    if max_val < value:
        max_val = value

ans = []
for key, value in books.items():
    if max_val == value:
        ans.append(key)
ans.sort()
print(ans[0])
