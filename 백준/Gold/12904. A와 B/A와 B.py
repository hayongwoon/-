# s -> t true, not false
# A 추가 or 뒤집고 B 추가
def from_s_to_t(s: str, t: str):
    s_list = list(s)
    t_list = list(t)
    while t_list:
        if t_list[-1] == "A":
            t_list.pop()
        else:
            t_list.pop()
            t_list.reverse()
        if t_list == s_list:
            return 1
    return 0

 
s = input()
t = input()
print(from_s_to_t(s, t))