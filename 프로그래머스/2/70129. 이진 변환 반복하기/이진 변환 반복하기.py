def solution(s):
    answer = [0,0]
    while s != '1':
        answer[1] += s.count('0')
        s = ''.join([x for x in s if x == '1'])
        s = format(len(s), 'b')
        answer[0] += 1
    return answer