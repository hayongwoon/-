def solution(order):
    answer = 0
    tmp = []
    i = 1
    while i != len(order) + 1:
        tmp.append(i)
        while tmp and tmp[-1] == order[answer]:
            answer += 1
            tmp.pop()
        i += 1
    return answer