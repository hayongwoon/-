def solution(extra: int) -> str:
    answer = [0, 0, 0, 0]
    while extra > 0:
        if extra >= 25:
            extra -= 25
            answer[0] += 1
        elif extra >= 10:
            extra -= 10
            answer[1] += 1
        elif extra >= 5:
            extra -= 5
            answer[2] += 1
        elif extra >= 1:
            extra -= 1
            answer[3] += 1
    return ' '.join([str(x) for x in answer])
        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(solution(extra=int(input())))