C = int(input())

for _ in range(C):
    N = list(map(int, input().split()))
    s = sum(N[1:])
    avg = s / N[0]

    cnt = 0
    for i in N[1:]:
        if i > avg:
            cnt += 1
    result = (cnt / N[0]) * 100
    result = round(result,3)

    print(f"{result:.3f}%")