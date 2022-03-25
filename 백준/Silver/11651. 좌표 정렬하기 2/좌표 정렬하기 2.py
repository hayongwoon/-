N = int(input())

result = []
for _ in range(N):
     result.append(list(map(int, input().split())))

result = sorted(result, key=lambda x: (x[1], x[0]))

for x, y in result:
    print(x, y)