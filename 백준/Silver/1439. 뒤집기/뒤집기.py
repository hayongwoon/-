def solution(s):
    cnt = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            cnt += 1
    return cnt // 2


if __name__ == '__main__':
    s = input()
    print(solution(s))
