text = input().split('-')

answer = 0
result = []
for i in text:
    try:
        result.append(int(i))

    except:
        result.append(i)

for idx, val in enumerate(result):
    if type(val) is not int:
        val = val.split('+')
        val = sum([int(i) for i in val])

        result[idx] = val

answer = result[0]
for j in result[1:]:
    answer -= j

print(answer)