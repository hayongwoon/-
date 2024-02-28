def generate_max_num(number: str) -> int:
    number_list = list(number)
    for i in range(len(number_list)):
        if number_list[i] == '5':
            number_list[i] = '6'
    return int(''.join(number_list))


def generate_min_num(number: str) -> int:
    number_list = list(number)
    for i in range(len(number_list)):
        if number_list[i] == '6':
            number_list[i] = '5'
    return int(''.join(number_list))



if __name__ == '__main__':
    a, b = input().split()
    min_a = generate_min_num(a)
    min_b = generate_min_num(b)
    max_a = generate_max_num(a)
    max_b = generate_max_num(b)
    print(min_a+min_b, max_a+max_b)
