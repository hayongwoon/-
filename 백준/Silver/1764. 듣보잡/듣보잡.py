n, m = map(int, input().split())

unheard_name_list = [input() for _ in range(n)]
unseen_name_list = [input() for _ in range(m)]

answer = list(set(unheard_name_list) & set(unseen_name_list))

answer.sort()
print(len(answer))
for name in answer:
    print(name)