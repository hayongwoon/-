def solution(k, score):
    answer = []
    honor_list = []
    for i in range(len(score)):
        answer.append(score[:i+1])
    for x in answer:
        x.sort(reverse=True)
        if len(x) > k:
            honor_list.append(x[k-1])
        else:
            honor_list.append(x[-1])
    return honor_list