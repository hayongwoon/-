# 약수의 갯수 리스트
# 초과하는 수는 power로 수정 후 합
def solution(number, limit, power):
    answer = []
    for i in range(1, number+1):
        yaksu = 0
        for j in range(1, int(i**0.5)+1):
            if (i) % (j) == 0:
                yaksu += 2
            if j**2 == i:
                yaksu -= 1
        if yaksu > limit:
            yaksu = power
        answer.append(yaksu)
    return sum(answer)