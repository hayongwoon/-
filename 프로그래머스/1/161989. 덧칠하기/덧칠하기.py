# 1. section에서 처음 나온 수 + m 까지 section에 있는 수를 지운다. answer += 1
# 2. section의 다음 처음 나온 수 + m까지 지우고 answer += 1 section이 없으면 종료
def solution(n, m, section):
    answer = 1
    pointer = section[0]
    next_pointer = pointer + m - 1
    for x in section:
        if x > next_pointer:
            answer += 1
            next_pointer = x + m - 1
    return answer