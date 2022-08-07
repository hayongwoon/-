from collections import defaultdict


def solution(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return solution(20, 20, 20)

    if a < b and b < c:
        if not dp[(a, b, c)]:
            dp[(a, b, c)] = solution(a, b, c-1) + solution(a, b-1, c-1) - solution(a, b-1, c)
        
        return dp[(a, b, c)]

    else:
        if not dp[(a, b, c)]:
            dp[(a, b, c)] = solution(a-1, b, c) + solution(a-1, b-1, c) + solution(a-1, b, c-1) - solution(a-1, b-1, c-1)

        return dp[(a, b, c)]


dp = defaultdict(int)
while 1:
    a, b, c = map(int,input().split())
    if all((a == -1, b == -1, c == -1)):
        break
    
    print(f'w({a}, {b}, {c}) = {solution(a, b, c)}')