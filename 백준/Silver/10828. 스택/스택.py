# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
t = int(sys.stdin.readline())

stack = []
for _ in range(t):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push':
        n = order[1]
        stack.append(int(n))
    if order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if order[0] == 'size':
        print(len(stack))
    if order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)