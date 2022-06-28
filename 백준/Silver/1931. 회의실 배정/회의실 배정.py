n = int(input())
meeting_times = [tuple(map(int, input().split())) for _ in range(n)]

meeting_times.sort(key=lambda x: (x[1], x[0]))
stack = [meeting_times[0]]

for i in meeting_times[1:]:
    if i[0] >= stack[-1][1]:
        stack.append(i)

print(len(stack))