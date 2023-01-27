word = input()
u_word = word.upper()

word_dict = {}
for word in u_word:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

max_list = list(sorted(word_dict.values(),reverse=True))
max_word = max(word_dict, key=lambda x:word_dict.get(x))

if len(max_list) == 1:
    print(max_word)
    
elif max_list[0] == max_list[1]:
    print('?')

else:
    print(max_word)