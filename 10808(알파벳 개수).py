S = input()
word = [0] * 26
for s in S:
    word[ord(s)-ord('a')] += 1
print(*word)
