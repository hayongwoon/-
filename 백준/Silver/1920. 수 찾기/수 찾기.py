n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

A = {v: k for k, v in enumerate(n_list, 1)}

for i in m_list:
    try:
        A[i]
        print(1)
    except KeyError:
        print(0)