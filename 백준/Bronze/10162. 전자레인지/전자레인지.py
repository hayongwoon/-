operating_times = [300, 60, 10]

cook_time = int(input())

answer = []
for t in operating_times:
    if cook_time >= t:
        answer.append(cook_time // t)
        cook_time = cook_time % t
    else:
        answer.append(0)

if cook_time:
    print(-1)
else:
    for i in answer:
        print(i, end=' ')