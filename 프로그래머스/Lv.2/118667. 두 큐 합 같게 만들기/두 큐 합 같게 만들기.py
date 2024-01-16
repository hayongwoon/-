from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    avg = (s1 + s2) // 2
    limit = len(queue1) * 3
    if (s1 + s2) % 2:
        return -1
    while s1 != s2:
        if s1 > s2:
            val = queue1.popleft()
            queue2.append(val)
            s1 -= val
            s2 += val
        elif s2 > s1:
            val = queue2.popleft()
            queue1.append(val)
            s1 += val
            s2 -= val
        answer += 1
        if answer == limit:
            return -1
    return answer