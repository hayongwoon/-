T = int(input())

for _ in range(T):
    K, N = map(int, input().split())

    A = 1
    for i in range(N,N-K,-1):
        A *= i

    B = 1
    for j in range(1,K+1):
        B *= j

    print(int(A/B))