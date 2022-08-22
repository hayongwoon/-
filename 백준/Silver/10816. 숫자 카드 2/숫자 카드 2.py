from collections import defaultdict


n = int(input())
card_number_list = list(map(int, input().split()))

m = int(input())
how_many_number_cards_list = list(map(int, input().split()))

number_of_cards_dict = defaultdict(int)
for card_number in card_number_list:
    number_of_cards_dict[card_number] += 1


for number in how_many_number_cards_list:
    print(number_of_cards_dict[number], end=' ')