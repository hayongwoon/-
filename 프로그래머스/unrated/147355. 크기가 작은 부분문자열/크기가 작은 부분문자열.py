def solution(t, p):
    answer = 0
    # t[0:len(p)], t[1:len(p)+1] ... t[len(p)-3:len(t)]
    for i in range(len(t)):
        if len(t[i:len(p)+i]) == len(p) and int(t[i:len(p)+i]) <= int(p):
            answer += 1
    return answer