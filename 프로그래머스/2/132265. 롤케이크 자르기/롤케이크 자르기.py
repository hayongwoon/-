from collections import Counter

def solution(topping):
    answer = 0
    stack = set()
    topping_dic = Counter(topping)
    while topping:
        val = topping.pop()
        stack.add(val)
        topping_dic[val] -= 1
        if topping_dic[val] == 0:
            topping_dic.pop(val)
        if len(stack) == len(topping_dic):
            answer += 1
    return answer