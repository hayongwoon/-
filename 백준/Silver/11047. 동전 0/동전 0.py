n, k = map(int, input().split())

pay_values = [int(input()) for _ in range(n)]
answer = 0
while k:
    value = pay_values.pop()

    if value <= k:
        answer += k // value
        k = k % value
        

print(answer)