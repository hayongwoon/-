from itertools import combinations


number_of_card, target_number = map(int, input().split())
card_list = list(map(int, input().split()))

answer = target_number
cards_combinations = combinations(card_list, 3)
for cards_combination in cards_combinations:
    difference_of_result = target_number - sum(cards_combination)
    if difference_of_result >= 0:
        answer = min(answer, difference_of_result)
        
print(target_number - answer)