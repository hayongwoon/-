from collections import deque


def solution(a, b):
    turn = 1
    q = deque()
    visited = set()
    q.append((a, turn))
    while q:
        value, turn = q.popleft()
        v1 = (value * 10) +  1
        v2 = value*2
        turn += 1
        if  v1 <= b and v1 not in visited:
            visited.add(v1)
            q.append((v1, turn))
        if v2 <= b and v2 not in visited:
            visited.add(v2)
            q.append((v2, turn))
        if v1 == b or v2 == b:
            return turn
    return -1


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solution(a, b))
