from collections import deque, defaultdict


def bfs(start_num):
    cnt_dict = defaultdict(int)
    q = deque()
    q.append(start_num)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        cur_num = q.popleft()

        if cur_num == '123456780':
            return cnt_dict[cur_num]

        zero_idx = cur_num.find('0')
        zero_x = zero_idx // 3
        zero_y = zero_idx % 3
        for i in range(4):
            zero_nx = zero_x + dx[i]
            zero_ny = zero_y + dy[i]

            if 0<=zero_nx<3 and 0<=zero_ny<3:
                next_zero_idx = (zero_nx * 3) + zero_ny
                next_num = list(cur_num)
                next_num[zero_idx], next_num[next_zero_idx] = next_num[next_zero_idx], next_num[zero_idx]
                next_num = ''.join(next_num)
                
                if not cnt_dict[next_num]:
                    cnt_dict[next_num] = cnt_dict[cur_num] + 1
                    q.append(next_num)
                
            
start_num = ''
for _ in range(3):
    start_num += input()
start_num = start_num.replace(" ", "")

result = bfs(start_num)
print(result if result != None else "-1" )