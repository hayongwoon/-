n, m = map(int, input().split())

unheard_name_list = []
unseen_name_list = []
for i in range(n+m):
    name = input()
    if i < n:
        unheard_name_list.append(name)
    
    else:
        unseen_name_list.append(name)

answer = list(set(unheard_name_list) & set(unseen_name_list))

answer.sort()
print(len(answer))
if answer:
    for name in answer:
        print(name)