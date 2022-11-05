# def solution(n):
#     ans = 0
#     n = n
#
#     return cnt(n, ans)
#
# def cnt(n, ans):
#     if n == 1:
#         ans += 1
#         return ans
#
#     if n % 2 == 1:
#         ans += 1
#         n = n // 2
#         return cnt(n, ans)
#     else:
#         n = n // 2
#         return cnt(n, ans)
#

def solution(n):
    ans = 1
    while n > 1:
        ans += n % 2
        n = n // 2
    return ans


print(solution(6))

