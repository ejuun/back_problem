N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
# cal = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         cal[i][j] = arr[i][j]

def mul(N, cal1, cal2):
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                    new_arr[i][j] += cal1[i][k] * cal2[k][j]
            new_arr[i][j] = new_arr[i][j] % 1000
    # for i in range(N):
    #     for j in range(N):
    #         cal[i][j] = new_arr[i][j]

    return new_arr

def recur(matrix, M):
    if M == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix

    elif M == 2:
        return mul(N, matrix, matrix)

    else:
        square = recur(matrix, M//2)

        if M % 2 == 0:
            return mul(N, square, square)
        else:
            return mul(N, mul(N, square, square), matrix)

ans = recur(arr, M)
for line in ans:
    print(*line)