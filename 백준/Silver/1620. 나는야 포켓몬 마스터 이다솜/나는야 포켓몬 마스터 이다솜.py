n, m = map(int, input().split())

pocketmon_name_list = [input() for _ in range(n)]
pocketmon_name_dict = {pocketmon: idx for idx, pocketmon in enumerate(pocketmon_name_list, 1)}

for _ in range(m):
    problem = input()
    if problem.isalpha():
        print(pocketmon_name_dict[problem])
    
    else:
        print(pocketmon_name_list[int(problem)-1])