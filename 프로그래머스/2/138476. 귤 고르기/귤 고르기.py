from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter_dict = Counter(tangerine)
    sorted_counter = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    for x, counter in sorted_counter:
        if k <= 0:
            break
        k -= counter
        answer += 1
    return answer