# 배수일때 식의 변화가 있어야 되는 것을 알았음에도 
# 어떻게 변경할지 몰라 결국 인터넷에서 찾음

T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    side = (N // H) +1
    floor = N % H
    if  N % H == 0:
        side = (N // H)
        floor = H
    print(100 * floor + side)
