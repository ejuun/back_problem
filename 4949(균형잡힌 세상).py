

while True:
    stack = []
    word = input()
    if len(word) == 1 and word == '.':
        break
    for w in word:
        if w == '(':
            stack.append(w)
        elif w == '[':
            stack.append(w)
        elif w == ')':
            if len(stack) >=1 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w)
        elif w == ']':
            if len(stack) >=1 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(w)
    if stack:
        print('no')
    else:
        print('yes')