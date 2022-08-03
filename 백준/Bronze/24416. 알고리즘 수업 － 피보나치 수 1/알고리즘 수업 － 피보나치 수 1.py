recursion_fibo_cnt = 0
def fib(n):
    global recursion_fibo_cnt

    recursion_fibo_cnt += 1
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

dp_fibo_cnt = 0
def fibonacci(n):
    global dp_fibo_cnt

    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        dp_fibo_cnt += 1
        f[i] = f[i-1] + f[i-2]

    return f[n]

n = int(input())
print(fibonacci(n), dp_fibo_cnt)