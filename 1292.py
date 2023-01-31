A,B = map(int,input().split())
num_list = []
for i in range(1,46):
    for j in range(i):
        num_list.append(i)

print(sum(num_list[A-1:B]))


# num_list = []
# for i in range(A,B+1):
#     for j in range(1,i+1):
#         num_list.append(i) 
# print(num_list)