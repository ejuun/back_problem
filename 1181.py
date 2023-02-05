N= int(input())
word_set = set()
for i in range(N):
    word = input()
    word_set.add(word)
word_list = list(word_set)
sort_list = sorted(word_list, key= lambda x : (len(x),x[0],x))
for word in sort_list:
    print(word)