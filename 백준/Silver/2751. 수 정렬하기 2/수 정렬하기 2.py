def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    # 남아있는 값들 전부 추가
    if array1_index:
        result += array2[array2_index:]

    if array2_index:
        result += array1[array1_index:]

    return result


def sorted_merge(arr):
    # 재귀 종료
    if len(arr) == 1:
        return arr
    
    # 재귀적으로 배열을 1개로 쪼개는 작업
    arr1, arr2 = sorted_merge(arr[len(arr)//2:]), sorted_merge(arr[:len(arr)//2])

    # 해당 배열들을 순서대로 정렬
    return merge(arr1, arr2)

n = int(input())
arr = [int(input()) for _ in range(n)]

for i in sorted_merge(arr):
    print(i)