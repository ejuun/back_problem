A = int(input())
B = int(input())
c = int(input())

multiple = A * B * c
c_0 = 0
c_1 = 0
c_2 = 0
c_3 = 0
c_4 = 0
c_5 = 0
c_6 = 0
c_7 = 0
c_8 = 0
c_9 = 0
for num in str(multiple):
    if num == '0':
        c_0 += 1
    elif num =='1':
        c_1 += 1
    elif num =='2':
        c_2 += 1
    elif num =='3':
        c_3 += 1
    elif num =='4':
        c_4 += 1
    elif num =='5':
        c_5 += 1
    elif num =='6':
        c_6 += 1
    elif num =='7':
        c_7 += 1
    elif num =='8':
        c_8 += 1
    elif num =='9':
        c_9 += 1
print(c_0)
print(c_1)
print(c_2)
print(c_3)
print(c_4)
print(c_5)
print(c_6)
print(c_7)
print(c_8)
print(c_9)

