n, l = map(int, input().split())
froots_height = [int(x) for x in input().split()]
froots_height.sort()
for x in froots_height:
    if l >= x:
        l += 1
    else:
        break
print(l)