n = int(input())
p_time = list(map(int, input().split()))

p_time.sort()

result = [p_time[0]]
for i in p_time[1:]:
    result.append(result[-1] + i)

print(sum(result))