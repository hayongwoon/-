n, l = map(int, input().split())
places = list(map(int, input().split()))
places.sort(reverse=True)

answer = []
while places:
    first = places.pop()
    stack = [first]
    while places:
        if places[-1] >= first + l:
            break
        stack.append(places.pop())
    answer.append(stack)
print(len(answer))