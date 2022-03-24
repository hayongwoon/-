T = int(input())

for _ in range(T):
    H, W, guest_cnt = map(int, input().split())
    floor = guest_cnt % H
    room = guest_cnt // H + 1

    if guest_cnt % H == 0:
        floor = H
        room = guest_cnt // H
        
    if room < 10:
        room = '0' + str(room)

    result = str(floor)+str(room)
    print(int(result))