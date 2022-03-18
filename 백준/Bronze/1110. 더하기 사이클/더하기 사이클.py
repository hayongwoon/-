N = int(input())

origin_val = N
cnt = 0
while 1:
    a = origin_val // 10
    b = origin_val % 10
    c = a + b

    next_val = (b * 10) + (c % 10)
    cnt += 1
    if next_val == N:
        print(cnt)
        break
    else:
        origin_val = next_val