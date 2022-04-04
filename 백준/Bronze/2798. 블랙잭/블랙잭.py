from itertools import combinations

N, M = map(int, input().split())
cards_num = sorted(list(map(int, input().split()))) #정렬 리스트

for idx, val in enumerate(cards_num[::-1]): #큰 수 부터
    if val < M:
        new_idx = len(cards_num) - idx #M 보다 작은 수부터 시작할 수 있도록 작은 수 기준 index 추출
        break

cards_num = cards_num[:new_idx]

combi_list = list(combinations(cards_num, 3)) #세 개의 수 조합 리스트를 만든다.
result = []
for i in combi_list:
    combi_sum = sum(i)
    if combi_sum <= M:
        result.append(combi_sum)

print(max(result))