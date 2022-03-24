a, b = map(int, input().split())

a_measure = [i for i in range(1,a+1) if a % i == 0]
b_measure = [j for j in range(1,b+1) if b % j == 0]

for k in b_measure[::-1]:
    if k in a_measure:
        common_factor = k
        print(common_factor)
        break



print(common_factor * (a // common_factor) * (b // common_factor))
