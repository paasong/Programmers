# from collections import deque
#
# def solution(prices):
#     answer = []
#     prices = deque(prices)
#
#     while prices:
#         sec = 0
#         stack = prices.popleft()
#         for p in prices:
#             sec += 1
#             if stack > p:
#                 break
#         answer.append(sec)
#     return answer
#
# print(solution([1, 1, 1, 1, 1]))

def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]
    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]: #stack이 없던지
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


print(solution([1, 2, 3, 2, 3]))