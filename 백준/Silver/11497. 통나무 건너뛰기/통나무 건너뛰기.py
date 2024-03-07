# 숫자 배열이 주어지면, 양 끝에 작은거 부터 채워넣어서 가운데가 가장 크게 배열을 정렬
# 옆에 수와 차이가 가장 큰 차이를 출력
def get_center_sorted(int_list: list[int]):
    int_list.sort()
    odd_list = int_list[1::2]
    odd_list.sort(reverse=True)
    return int_list[0::2] + odd_list


def get_max_diff(int_list: list[int]):
    i = 0
    result = 0
    while i != len(int_list)-1:
        result = max(result, abs(int_list[i] - int_list[i-1]), abs(int_list[i] - int_list[i+1]))
        i += 1
    return result


answer = []
t = int(input())
for _ in range(t):
    n = int(input())
    answer.append(get_max_diff(get_center_sorted(list(map(int, input().split())))))

for x in answer:
    print(x)
