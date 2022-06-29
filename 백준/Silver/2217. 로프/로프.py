n = int(input())

weights = [int(input()) for _ in range(n)]
weights.sort(reverse=True)

answer = max(weights)
for i, w in enumerate(weights, 1):
    answer = max(i*w, answer)

print(answer)