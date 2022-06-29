exchanges = [500, 100, 50, 10, 5, 1]

price = int(input())
pay = 1000
get_money = pay - price

answer = 0
for e in exchanges:
    if e <= get_money:
        answer += get_money // e
        get_money = get_money % e

print(answer)