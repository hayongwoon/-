def solution(cards1, cards2, goal):
    answer = 'Yes'
    while goal:
        char = goal.pop(0)
        if cards1 and char == cards1[0]:
            cards1.pop(0)
        elif cards2 and char == cards2[0]:
            cards2.pop(0)
        else:
            answer = 'No'
            break
    return answer