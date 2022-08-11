n = int(input())
length_info_list = []
for _ in range(6):
    direction, length = map(int, input().split())
    length_info_list.append((direction, length))


# 큰 사각형을 구하기 
row_list = []
column_list = []
for length_info in length_info_list:
    if length_info[0] == 1 or length_info[0] == 2:
        row_list.append(length_info[1]) 

    if length_info[0] == 3 or length_info[0] == 4:
        column_list.append(length_info[1])

# 큰사각형의 가로, 세로
large_row_length = max(row_list)
large_column_length = max(column_list)
row_column_max_length = [large_row_length, large_column_length]

#[(4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100), (4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100)]
#   r         c                  x        y
#[(3, 20), (1, 100), (4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100), (4, 50), (2, 160), (3, 30), (1, 60)]
#                       r        c                  x         y
#[(3, 30), (1, 60), (3, 20), (1, 100), (4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100), (4, 50), (2, 160)]
#                                         r        c                  x        y

# 작은 사각형의 가로 세로 x, y의 길이는 r을 기준으로 3칸과 4칸 뒤에 있는 값이다.
double_length_info_list = length_info_list * 2

for i in range(len(double_length_info_list)):
    if double_length_info_list[i][1] in row_column_max_length:
        if double_length_info_list[i+1][1] in row_column_max_length:
            small_row_length = double_length_info_list[i+3][1]
            small_column_length = double_length_info_list[i+4][1]

            print((large_row_length*large_column_length - small_row_length*small_column_length) * n)
            break