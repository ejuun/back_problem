import sys

input = sys.stdin.readline

roma = {'A': -1, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for _ in range(int(input())):
    number = list(input().rstrip())
    if number[0].isdigit():
        ans = []
        for i in range(len(number)):
            if int(number[i]) == 4:
                if len(number) - i == 3:
                    ans.append('CD')
                elif len(number) - i == 2:
                    ans.append('XL')
                else:
                    ans.append('IV')
            elif int(number[i]) == 9:
                if len(number) - i == 3:
                    ans.append('CM')
                elif len(number) - i == 2:
                    ans.append('XC')
                else:
                    ans.append('IX')
            elif int(number[i]) >= 5:
                if len(number) - i == 3:
                    ans.append('D')
                elif len(number) - i == 2:
                    ans.append('L')
                else:
                    ans.append('V')
            if 0 < int(number[i]) < 4 or 5 < int(number[i]) < 9:
                if int(number[i]) > 5:
                    number[i] = int(number[i]) - 5
                for _ in range(int(number[i])):
                    if len(number) - i == 4:
                        ans.append('M')
                    elif len(number) - i == 3:
                        ans.append('C')
                    elif len(number) - i == 2:
                        ans.append('X')
                    else:
                        ans.append('I')
        answer = ''
        for i in range(len(ans)):
            answer += ans[i]
        print(answer)
    else:
        ans = 0
        idx = 0
        number = number + ['A']
        while idx < len(number)-1:
            if roma[number[idx]] < roma[number[idx+1]]:
                n = roma[number[idx+1]] - roma[number[idx]]
                ans += n
                idx += 2
            else:
                ans += roma[number[idx]]
                idx += 1
        print(ans)
