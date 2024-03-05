def solution(s: str):
    answer = ''
    temp = ''
    for i in range(len(s)):
        x = s[i]
        temp += x
        if temp == 'XXXX':
            answer += 'AAAA'
            temp = ''
        elif x == '.':
            if temp == 'X.' or temp == 'XXX.':
                return -1
            elif temp == 'XX.':
                answer += 'BB'
            answer += '.'
            temp = ''
        elif i == len(s)-1:
            if temp == 'XX':
                answer += 'BB'
            elif temp == 'X' or temp == 'XXX':
                return -1
    if not answer:
        return -1
    else:
        return answer


print(solution(s=input()))
