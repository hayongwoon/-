M = int(input())
N = int(input())

def prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

result = [i for i in range(M, N+1) if prime_num(i)]

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)