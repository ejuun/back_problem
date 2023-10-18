N = int(input())

cnt = start = 0
end = 1

hap = start + end

while start <= end <= N:
    if hap < N:
        end += 1
        hap += end
    elif hap > N:
        hap -= start
        start += 1
    else:
        cnt += 1
        end += 1
        hap += end

print(cnt)