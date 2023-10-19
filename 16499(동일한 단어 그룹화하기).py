N = int(input())

words = set()
for _ in range(N):
    word = list(input())
    word.sort()
    words.add(tuple(word))
print(len(words))