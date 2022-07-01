n = list(input())

n.sort(reverse=True)

if int(n[-1]):
    print(-1)
else:
    n = n[:-1]
    s = sum([int(n[i]) for i in range(len(n))])
    if s % 3:
        print(-1)
    else:
        print(''.join(n) + str(0))