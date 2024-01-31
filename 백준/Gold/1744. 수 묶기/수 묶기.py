n = int(input())
suyeol = [int(input()) for _ in range(n)]

answer = 0
plus = []
minus = []
for x in suyeol:
    if x > 1:
        plus.append(x)
    elif x == 1:
        answer += x
    elif x <= 0:
        minus.append(x)
plus.sort()
minus.sort(reverse=True)

while len(plus) >= 2:
    answer += plus.pop()*plus.pop()
while len(minus) >= 2:
    answer += minus.pop()*minus.pop()

answer += sum(minus) + sum(plus)
print(answer)
# -1 1 2 3
# -1 1 2