N, S = map(int, input().split())
arr = list(map(int, input().split()))

length = 100000
end = 0
inter_sum = 0

for start in range(N):

    while inter_sum < S and end < N:
        inter_sum += arr[end]
        end += 1

    if inter_sum >= S:
        #end를 찍어보면 위에 while에서 end += 1하고 종료되기때문에 오른쪽으로 한 칸 더 이동한 상태이므로
        # -1를 해주면 원래 배열의 인덱스 or 값이 된다.
        if length > (end - 1) - start + 1:
            length = (end - 1) - start + 1

    inter_sum -= arr[start]

if length == 100000:
    length = 0

print(length)