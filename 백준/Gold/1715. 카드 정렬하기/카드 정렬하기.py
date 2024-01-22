import heapq


def solution(cards: list[int]) -> int:
    answer = 0 
    while len(cards) > 1:
        v1 = heapq.heappop(cards)
        v2 = heapq.heappop(cards)
        s = v1 + v2
        answer += s
        heapq.heappush(cards, s)
    return answer


if __name__ == '__main__':
    n = int(input())
    cards = []
    for _ in range(n):
        num = int(input())
        heapq.heappush(cards, num)
    print(solution(cards))