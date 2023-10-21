import math

S, T = map(int, input().split())

# nums = {'even': 0, 'odd': 0}
# for number in range(S, T + 1):
#     for num in range(1, int(math.sqrt(number)) + 1):
#         if number % num == 0:
#             if num % 2:
#                 nums['odd'] += 1
#             else:
#                 nums['even'] += 1
#
#             div = number // num
#             if div == num :
#                 continue
#             if div % 2:
#                 nums['odd'] += 1
#             else:
#                 nums['even'] += 1
#
# print(nums['even'] - nums['odd'])

def sol(x):
    ans = 0
    for i in range(1, x+1):
        if i % 2 == 0:
            ans += x // i
        else:
            ans -= x // i
    return ans

print(sol(T) - sol(S-1))