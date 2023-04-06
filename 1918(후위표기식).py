infix = input()
postfix = ''
stack = []

isp = {'+': 1, '*': 2, '-': 1, '/': 2, '(': 0, ')': 3}
icp = {'+': 1, '*': 2, '-': 1, '/': 2, '(': 3, ')': 3}

for token in infix:
    if token in isp:
        if token == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and icp[token] <= isp[stack[-1]]:
                postfix += stack.pop()
            stack.append(token)
    else:
        postfix += token
while stack:
    postfix += stack.pop()

print(postfix)