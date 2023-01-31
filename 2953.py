number_sum_list = [0]
for i in range(5):
    num_sum = 0
    score1,score2,score3,score4= map(int,input().split())
    num_sum += (score1 + score2 + score3 + score4)
    number_sum_list.append(num_sum)

max_sum = number_sum_list[0]
for i in range(len(number_sum_list)):
    if max_sum < number_sum_list[i]:
        max_sum = number_sum_list[i]

print(number_sum_list.index(max_sum),max_sum)
