A,B,V = map(int,input().split())

if A - B == 1:
    cnt = V - A +1
else:    
    if V // (A-B) == 0:
        cnt = 2
    else:
        if (V-A) % (A-B) == 0:
            cnt = ((V-A)//(A-B)) + 1
        else:
            cnt = ((V-A)//(A-B)) + 2
print(cnt)