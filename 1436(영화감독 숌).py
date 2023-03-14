N = int(input())
six_list = [0]
for i in range(666, 10000000):
    if '666' in str(i):
        six_list.append(i)
print(six_list[N])