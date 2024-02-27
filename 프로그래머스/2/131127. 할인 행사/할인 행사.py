from collections import defaultdict
from copy import deepcopy


def solution(want, number, discount):
    def check_all_zeros(lst):
        # 리스트 안에 모든 요소가 0인지 확인
        for elem in lst:
            if elem != 0:
                return False
        return True

    answer = 0
    want_info = defaultdict(int)
    for w, n in zip(want, number):
        want_info[w] = n
    for i in range(len(discount)-9):
        discount_10 = discount[i:i+10]
        _copy = deepcopy(want_info)
        for d in discount_10:
            _copy[d] -= 1
        if check_all_zeros(_copy.values()):
            answer += 1
    return answer