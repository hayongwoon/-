s = input()
answer = []
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in s:
        answer.append(str(s.index(x)))
    else:
        answer.append("-1")
print(" ".join(answer))