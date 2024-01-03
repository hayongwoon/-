def solution(s, skip, index):
    answer = []
    alphabets = [x for x in 'abcdefghijklmnopqrstuvwxyz' if x not in skip]
    hard_index = index
    for x in s:
        x_idx = alphabets.index(x) + index
        if x_idx > len(alphabets) - 1:
            next_alpha = alphabets[x_idx % len(alphabets)]
        else:
            next_alpha = alphabets[x_idx]
        answer.append(next_alpha)
    return ''.join(answer)