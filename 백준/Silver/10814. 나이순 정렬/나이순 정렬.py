n = int(input())

result = [input().split() for _ in range(n)]
result.sort(key=lambda x: int(x[0]))

for i in result:
    print(i[0], i[1])