def solution(order):
    answer = 0
    tmp = []
    for i in range(1, len(order) + 1):
        tmp.append(i)
        while tmp and tmp[-1] == order[answer]:
            answer += 1
            tmp.pop()
    return answer