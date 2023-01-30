N = int(input())
i = 0
cnt = 1
bee_sum = 1
while True:
    if N <= bee_sum + 6*i:       
        break
    else:
        bee_sum += 6*i
        i +=1
        cnt += 1
print(cnt)