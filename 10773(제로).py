K = int(input())
stack =[0]
for _ in range(K):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))