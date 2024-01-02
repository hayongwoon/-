# 1. '#' 의 좌표 정보를 받는다.
# 2. 좌표 정보 중 x값이 가장 작은 수를 0번째, 가장 큰 수 + 1를 2번 째
# 3. 좌표 정보 중 y값이 가장 작은 수를 1번째, 가장 큰 수 + 1를 3번 째
def solution(wallpaper):
    x_list = []
    y_list = []
    for x_index, x in enumerate(wallpaper):
        for y_index, y in enumerate(x):
            if y == '#':
                x_list.append(x_index)
                y_list.append(y_index)
                
    return [min(x_list), min(y_list), max(x_list) + 1, max(y_list) + 1]