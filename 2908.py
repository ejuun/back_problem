A,B = map(int, input().split())

a= []
b= []
for word in str(A):
    a.append(word)
for word in str(B):
    b.append(word)

r_a = a.reverse()
r_b = b.reverse()

r_A = ''.join(a)
r_B = ''.join(b)

if int(r_A) > int(r_B) :
    print(r_A)
else:
    print(r_B)
