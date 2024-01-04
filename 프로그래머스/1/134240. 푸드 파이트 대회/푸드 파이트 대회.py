def solution(food):
    answer = []
    for i, x in enumerate(food):
        amount = x // 2
        if amount > 0:
            answer.append(str(i)*amount)
    return ''.join(answer) + "0" + ''.join(answer[::-1])