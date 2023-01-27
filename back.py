N = list(map(int, input().split()))
a = True
d = True
for i in range(len(N)-1):
    if N[i] > N[i+1]:
        a = False
    elif N[i] < N[i+1]:
        d = False
if a:
    print('ascending')
elif d:
    print('descending')
else:
    print('mixed')


# sort_list = sorted(N)
# reverse_list = sorted(N,reverse=True)

# if sort_list == N :
#     print('asending')
# elif reverse_list == N:
#     print('descending')
# else:
#     print('mixed')