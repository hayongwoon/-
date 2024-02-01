def solution(n, m):
    sp = 1000
    op = 1000
    for _ in range(m):
        six_price, one_price = map(int, input().split())
        sp = min(sp, six_price)
        op = min(op, one_price)
    if op*6 <= sp:
        return op*n

    answer = 0
    while n > 0:
        if n < 6:
            if n*op <= sp:
                answer += n*op
            else:
                answer += sp
            return answer
        answer += sp
        n -= 6
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solution(n, m))