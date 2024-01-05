def solution(survey, choices):
    answer = ''
    type_info = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }
    for s, c in zip(survey, choices):
        point = c - 4
        if c - 4 > 0:
            type_info[s[1]] += abs(point)
        else:
            type_info[s[0]] += abs(point)
    if type_info["R"] >= type_info["T"]:
        answer += "R"
    else:
        answer += "T"
    if type_info["C"] >= type_info["F"]:
        answer += "C"
    else:
        answer += "F"
    if type_info["J"] >= type_info["M"]:
        answer += "J"
    else:
        answer += "M"
    if type_info["A"] >= type_info["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer