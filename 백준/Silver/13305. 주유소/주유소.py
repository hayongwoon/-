n = int(input())
distance_lst = list(map(int, input().split()))
price_lst = list(map(int, input().split()))

answer = 0

left = 0
right = left + 1
while right != len(price_lst):
    while price_lst[left] <= price_lst[right]:
        right += 1
        if right == len(price_lst) - 1:
            break

    for i in range(left, right):
        answer += distance_lst[i] * price_lst[left]
        
    left = right
    right = left + 1

print(answer)   
