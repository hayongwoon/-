n = int(input())
length_info_list = []
for _ in range(6):
    direction, length = map(int, input().split())
    length_info_list.append((direction, length))


row_list = []
column_list = []
for length_info in length_info_list:
    if length_info[0] == 1 or length_info[0] == 2:
        row_list.append(length_info[1]) 

    if length_info[0] == 3 or length_info[0] == 4:
        column_list.append(length_info[1])


row_max_length = max(row_list)
column_max_length = max(column_list)

[(4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100)]
#   x        y
[(3, 20), (1, 100), (4, 50), (2, 160), (3, 30), (1, 60)]
#                     x         y
[(3, 30), (1, 60), (3, 20), (1, 100), (4, 50), (2, 160)]
#                                        x        y

double_length_info_list = length_info_list * 2

for i in range(len(double_length_info_list)):
    if double_length_info_list[i][1] == row_max_length or double_length_info_list[i][1] == column_max_length:
        if double_length_info_list[i+1][1] == row_max_length or double_length_info_list[i+1][1] == column_max_length:
            x = double_length_info_list[i+3][1]
            y = double_length_info_list[i+4][1]

            print((row_max_length*column_max_length - x*y)*n)
            break