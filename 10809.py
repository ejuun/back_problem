S = input()
S_list = []
for str in S:
    S_list.append(str)
set_S = set(S_list)
for i in[chr(c) for c in range(ord('a'),ord('z')+1)]:
    if i in set_S:
        print(S_list.index(i),end=' ')
    else:
        print(-1,end=' ')