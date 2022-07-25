from collections import deque, defaultdict


def bfs(start_number, target_number):
    q = deque()
    q.append(start_number)
    distance_dict = defaultdict(int)
    distance_dict[start_number] = 0

    dx = [-1, 1]
    while q:
        cur_num = q.popleft()

        if cur_num == target_number:
            return distance_dict[cur_num]

        for i in range(3):
            if i < 2:
                next_num = cur_num + dx[i]
            else:
                next_num = cur_num*2

            if 0<=next_num<=100000 and not distance_dict[next_num]:
                distance_dict[next_num] = distance_dict[cur_num] + 1
                q.append(next_num)

start_number, target_number = map(int, input().split())
print(bfs(start_number, target_number))