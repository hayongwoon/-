def solution(babbling):
    answer = 0
    possible_words = ["aya", "ye", "woo", "ma"]
    for x in babbling:
        for word in possible_words:
            if word*2 not in x:
                x = x.replace(word, ' ')
        if x.isspace():
            answer += 1
    return answer