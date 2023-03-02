L, C = map(int, input().split())
word = sorted(list(map(str, input().split())))

arr = []

def back(start):
    if len(arr) == L:
        if 'a' in arr or 'e' in arr or 'i' in arr or 'o' in arr or 'u' in arr:
            if arr.count('a') + arr.count('e') + arr.count('i') + arr.count('o') + arr.count('u') <= len(arr)-2:
                print(''.join(arr))
        return

    for i in range(start, len(word)):
        if word[i] not in arr:
            arr.append(word[i])
            back(i)
            arr.pop()

back(0)