# def solution(n, s):
#     answer = []
#     if n>s:
#         return [-1]
#
#     if s%n == 0:
#         answer=[s/n for _ in range(n)]
#     else:
#         d_share = s//n
#         d_share += 1
#         answer = [ d_share for _ in range(n)]
#
#         for i in range((d_share*n)-s):
#             answer[i] -= 1
#
#     answer.sort()
#     return answer

def solution(n, s):
    if s < n:
        return [-1]
    answer = []

    for _ in range(n - s % n):
        print(s // n)
        answer.append(s // n)

    for _ in range(s % n):
        print(s//n+1)
        answer.append(s // n + 1)
    return answer

print(solution(3,7))