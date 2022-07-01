n = int(input())
answer = 1
while n:
    n -= answer
    if answer+1 > n:
        break

    answer += 1
print(answer)