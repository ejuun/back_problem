num_list = []
for i in range(10):
    number = int(input())
    num_list.append(number)

sum_number = 0
for i in range(len(num_list)):
    sum_number += num_list[i]
    if sum_number == 100:
        print(sum_number)
        break
    elif sum_number > 100:
        if (sum_number - 100) > (100 - (sum_number-num_list[i])):
            print(sum_number-num_list[i])
            break
        else:
            print(sum_number)
            break
else:
    print(sum_number)  