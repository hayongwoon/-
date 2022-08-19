n = int(input())

user_info_list = [input().split() for _ in range(n)]
user_info_list.sort(key=lambda x: int(x[0]))

for user in user_info_list:
    print(user[0], user[1])