def mother_num(num):
    for i in range(1, num):
        N = sum([int(i) for i in str(i)])

        if i+N == num:
            return i
    return 0


M = int(input())
print(mother_num(M))