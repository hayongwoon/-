n = int(input())
arr = [int(input()) for _ in range(n)]

sorted_arr = []
while arr:
    min_val = min(arr)
    sorted_arr.append(min_val)
    arr.remove(min_val)
    
for i in sorted_arr:
    print(i)