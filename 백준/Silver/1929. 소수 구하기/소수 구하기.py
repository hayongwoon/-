def prime_num(n):
    if n == 1:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

    return True

M, N = map(int, input().split())
if M == 1:
    M = 2
for i in range(M, N+1):
    if prime_num(i):
        print(i)