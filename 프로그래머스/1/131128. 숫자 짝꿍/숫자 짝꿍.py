def solution(X, Y):
    answer = []
    common = list(set(list(X)) & set(list(Y)))
    if not common:
        return '-1'
    if len(common) == 1 and common[0] == '0':
        return '0'
    common.sort(reverse=True)
    for x in common:
        min_count = min(list(X).count(x), list(Y).count(x))
        answer += list(min_count*x)
    return ''.join(answer)