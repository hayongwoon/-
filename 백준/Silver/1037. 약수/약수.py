N = int(input())

measure_num = sorted(list(map(int, input().split())))

result = measure_num[0]*measure_num[N-1]
print(result)
