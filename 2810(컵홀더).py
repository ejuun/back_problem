N = int(input())
seat = input()

new_seat = seat.replace('LL', 'L')

cup_cnt = len(new_seat) + 1

if N > cup_cnt:
    print(cup_cnt)
else:
    print(N)

