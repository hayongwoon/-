def solution(s):
    answer = []
    reverse_s = list(s[::-1])
    while reverse_s:
        first_alpha = reverse_s.pop(0)
        try:
            answer.append(reverse_s.index(first_alpha) + 1)
        except:
            answer.append(-1)
    return answer[::-1]