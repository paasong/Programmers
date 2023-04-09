# import sys
#
# num = int(sys.stdin.readline())
# answer = 1
#
# for i in range(num):
#     answer *= (i+1)
#
# print(answer)

# import sys
# num = int(sys.stdin.readline())
# answer = 1
# def factorial(num, answer):
#     if num < 1:
#         print(answer)
#         return 0
#     else:
#         answer *= num
#         return factorial(num-1, answer)
#
# factorial(num, answer)

# val = int(input())
# #
# # def factorial(num):
# #     if num <=0:
# #         return 1
# #     else:
# #         print(num)
# #         return num * factorial(num-1)
# #
# # print(factorial(val))

num = int(input())
def factorial(num):
    print('a',num)
    if num > 1:
        a = num * factorial(num-1)
        print('b',num)
        return a
    else:
        return num
print(factorial(num))