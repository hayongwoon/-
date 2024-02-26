from collections import defaultdict


def solution(weights):
    answer = 0
    ratios = [1, 2/3, 1/2, 3/4, 3/2, 2, 4/3]
    all_weights = defaultdict(int)
    for w in weights:
        for r in ratios:
            answer += all_weights[w*r]
        all_weights[w] += 1
    return answer