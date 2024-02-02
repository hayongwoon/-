def solution(exchange):
    answer = 0
    if exchange == 1 or exchange == 3:
        return -1
    if (exchange % 5) % 2 == 0:
        answer = (exchange // 5) + (exchange % 5) // 2
    else:
        num_5 = (exchange // 5) - 1
        answer = num_5 + (exchange - num_5*5) // 2
    return answer


exchange = int(input())
print(solution(exchange=exchange))