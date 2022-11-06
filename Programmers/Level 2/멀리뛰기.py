def solution(n):
    if n < 2:
        return n

    ans = [1, 2]
    for _ in range(n-2):
        ans.append(ans[-1]+ans[-2])

    return ans[-1]


print(solution(4))



# from itertools import permutations
# def solution(n):
#     bin_n = bin(n)[2:]
#     cnt_2 = 0
#     cnt_1 = 0
#     ans = 0
#
#     if bin_n[-1] == '1':
#         cnt_1 = 1
#     for i in enumerate(bin_n[::-1]):
#         if i[1] == "1":
#             cnt_2 += 2**i[0]//2
#
#     list_2 = [2 for _ in range(cnt_2)]
#     list_1 = [1 for _ in range(cnt_1)]
#
#     while cnt_2 >= 0 :
#         list_2.extend(list_1)
#         ans += len(set(permutations(list_2, len(list_2))))
#
#
#         cnt_2 -= 1
#         cnt_1 += 2
#         del list_2[0]
#         list_1.extend([1, 1])
#     return ans % 1234567


# def solution(n):
#     if n == 1 :
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return solution(n - 1) + solution(n - 2) % 1234567
