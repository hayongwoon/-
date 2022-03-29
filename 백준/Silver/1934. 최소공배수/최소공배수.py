T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    for i in range(A,0,-1):
        if B % i == 0 and A % i == 0:
            print((B * A) // i)
            break