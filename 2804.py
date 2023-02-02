A, B = input().split()
for i in range(len(A)):
    if A[i] in B:
        b_start_index = i
        a_start_index = B.index(A[i])
        break

for i in range(len(B)):
    if i == a_start_index:
        print(A, end='')
    for j in range(len(A)):
        if i == a_start_index:
            break
        if j == b_start_index:
            print(B[i], end='')
        else:
            print('.', end='')
    if i == len(B)-1:
        break
    else:
        print('')
