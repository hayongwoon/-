s_list = list(input())
n = int(input())
stack = []

for _ in range(n):
    user_commend = input()

    if user_commend[0] == 'L' and s_list:
        stack.append(s_list.pop())

    if user_commend[0] == 'D' and stack:
        s_list.append(stack.pop())

    if user_commend[0] == 'B' and s_list:
        s_list.pop()

    if user_commend[0] == 'P':
        s_list.append(user_commend[-1])
            

print(''.join(s_list + list(reversed(stack))))