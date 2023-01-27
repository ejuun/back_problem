num_list = []
for i in range(10):
    num = int(input())
    num_list.append(num)

reminder = []
for num in num_list:
    re = num % 42
    reminder.append(re) 

cnt_reminder = len(set(reminder))
print(cnt_reminder)