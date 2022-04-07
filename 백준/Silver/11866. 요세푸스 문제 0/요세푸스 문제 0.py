N, K = map(int, input().split())

lst_N = [i for i in range(1, N+1)] #처음 리스트

result = []
sun = 0
for j in range(N):
    sun += K - 1 #pop 인덱스
    if sun >= len(lst_N): #한바퀴 돌면 다시 sun
        sun = sun % len(lst_N)

    result.append(str(lst_N.pop(sun)))

print("<",", ".join(result)[:],">", sep='')