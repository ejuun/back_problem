A, K = map(int, input().split())

cnt = 0
while True:
    if K == A:
        break

    elif K > A:
        if K % 2: #홀수일떄
            K -= 1
            cnt += 1
        #짝수일때 2로 나눴을떄도 A보다 크다면 그대로 나누기
        if K // 2 > A:
            K = K // 2
            cnt += 1
        #만약 2로 나눈값이 A보다 작다면
        elif K // 2 < A:
            #A 가 될때까지 1씩 뺴주기기
           while K != A:
                K -= 1
                cnt += 1
        #2로 나눴을때 A와 같아진다면 cnt += 1하기
        else:
            K = K // 2
            cnt += 1
print(cnt)