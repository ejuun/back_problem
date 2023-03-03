N = int(input())
for _ in range(N):
    A, *A_card = map(int, input().split())
    B, *B_card = map(int, input().split())

    if A_card.count(4) > B_card.count(4):
        print('A')
    elif A_card.count(4) < B_card.count(4):
        print('B')
    else:
        if A_card.count(3) > B_card.count(3):
            print('A')
        elif A_card.count(3) < B_card.count(3):
            print('B')
        else:
            if A_card.count(2) > B_card.count(2):
                print('A')
            elif A_card.count(2) < B_card.count(2):
                print('B')
            else:
                if A_card.count(1) > B_card.count(1):
                    print('A')
                elif A_card.count(1) < B_card.count(1):
                    print('B')
                else:
                    print('D')