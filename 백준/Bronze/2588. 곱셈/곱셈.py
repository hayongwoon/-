n1 = input()
n2 = input()

#3,2,1
for i in range(3, 0, -1):
    result = int(n1)*int(n2[i-1])
    print(result)
print(int(n1)*int(n2))