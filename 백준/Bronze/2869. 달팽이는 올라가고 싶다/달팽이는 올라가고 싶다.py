import math

up_stair, down_stair, tree_height = map(int, input().split())

day = math.ceil((tree_height-up_stair)/(up_stair-down_stair)) + 1

print(day)