N = int(input())

result = []
for _ in range(N):
    _order = int(input())
    if _order != 0:
        result.append(_order)
    else:
        result.pop()

print(sum(result))