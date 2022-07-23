# 3*7=21, 3*10=30 -> 30
# 4*7=28, 2*10=20 -> 28

def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer