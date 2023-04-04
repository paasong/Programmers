import re
def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    print(s)
    s = [i.split(',') for i in s]
    print(s)
    s.sort(key=lambda x:len(x))

    print('1',s)

    answer.append(int(s[0][0]))

    for i in range(1,len(s)):
        num = set(s[i])-set(s[i-1])
        answer.append(int(num.pop()))

    print('2',answer)

    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

# def solution(s):
#     answer = []
#
#     s1 = s.lstrip('{').rstrip('}').split('},{')
#     print(s1)
#
#     new_s = []
#     for i in s1:
#         new_s.append(i.split(','))
#
#     new_s.sort(key = len)
#
#     for i in new_s:
#         for j in range(len(i)):
#             if int(i[j]) not in answer:
#                 answer.append(int(i[j]))
#
#     return answer
