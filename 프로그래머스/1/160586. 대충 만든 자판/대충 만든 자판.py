# 1. 문자와 인덱스 정보가 담긴 dict를 만든다.
# 2. target 반복문으로 합을 구한다.
from collections import defaultdict


def solution(keymap, targets):
    answer = []
    char_info = defaultdict(int)
    for chars in keymap:
        for i, char in enumerate(chars):
            if char in char_info:
                if char_info[char] > i + 1:
                    char_info[char] = i + 1
            else:
                char_info[char] = i + 1
    for i in targets:
        target_sum = 0
        for j in i:
            if char_info[j]:
                target_sum += char_info[j]
            else:
                target_sum = -1
                break
        answer.append(target_sum)
    return answer