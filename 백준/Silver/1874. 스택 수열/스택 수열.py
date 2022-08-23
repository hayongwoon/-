def sequence_of_stack(result, result_idx=0, number=1): 
    stack = []
    sequence = []
    answer = []
    while sequence != result: 
        if stack and stack[-1] == result[result_idx]:
            pop_number = stack.pop()
            result_idx += 1
            sequence.append(pop_number)
            answer.append('-')

        else:
            stack.append(number)
            answer.append('+')
            number += 1

        if len(stack) > n:
            return 'NO'

    return '\n'.join(answer)


n = int(input())
result = [int(input()) for _ in range(n)]
print(sequence_of_stack(result))