n = int(input())
level_points = [int(input()) for _ in range(n)]
answer = 0
while level_points:
    next_point = level_points.pop()
    if level_points and next_point <= level_points[-1]:
        back_level = level_points[-1]
        level_points[-1] = next_point - 1
        answer += back_level - level_points[-1]
print(answer)
