def solution(storey):
    answer = 0
    per_number = [int(x) for x in list(str(storey))]
    while per_number:
        number = per_number.pop()
        if number < 5:
            answer += number
        elif 5 < number:
            answer += 10-number
            if per_number:
                per_number[-1] += 1
            else:
                per_number.append(1)
        else:
            if per_number and per_number[-1] >= 5:
                per_number[-1] += 1
            answer += number
    return answer