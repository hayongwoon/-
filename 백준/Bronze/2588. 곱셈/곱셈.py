a= int(input())
b= int(input())
b1= reversed(str(b))
for i in b1:
    print(a*int(i))
print(a*b)