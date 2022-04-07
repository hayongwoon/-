wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1

for j in range(0, 98):
    wh[j+3] = wh[j] + wh[j+1]


T = int(input())

for _ in range(T):
    n = int(input())
    print(wh[n])