N = int(input())
hap = 0
dic = dict()
num = [0] * N
for i in range(N):
    n = int(input())

    hap += n
    num[i] = n

    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

num.sort()

if hap < 0:
    mean = -hap
    mean = mean/N
    one = round(-mean)
else:
    one = round(hap/N)
#========================================
two = num[N//2]
#========================================
max_cnt = 0
for value in dic.values():
    if max_cnt <= value:
        max_cnt = value
able =[]
for key, value in dic.items():
    if max_cnt == value:
       able.append(key)
able.sort()
if len(able)==1:
    three = able[0]
else:
    three = able[1]
#========================================
if len(num) == 1:
    four = 0
else:
    four = num[N-1] - num[0]
#========================================
print(one)
print(two)
print(three)
print(four)

