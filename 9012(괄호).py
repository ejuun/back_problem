for tc in range(int(input())):
    stack = []
    ps = input()

    for st in ps:
        if st == '(':
            stack.append(st)
        else:
            if len(stack) >= 1 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(st)
                break
    if stack:
        print('NO')
    else:
        print('YES')
