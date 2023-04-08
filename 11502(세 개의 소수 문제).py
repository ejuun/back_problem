for _ in range(int(input())):
    K = int(input())

    num = [0] * (K+1)
    num[0] = num[1] = 1
    for i in range(2, K+1):
        if not num[i]:
            for j in range(i*2, K+1, i):
                num[j] = 1
    prime = []
    for i in range(len(num)):
        if not num[i]:
            prime.append(i)

    ans = 0
    for i in prime:
        for j in prime:
            for k in prime:
                if i + j + k == K:
                    print(i, j, k)
                    ans = 1
                    break
            if ans:
                break
        if ans:
            break
    else:
        print(0)
