import re

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    a, b = list(), list()
    for  i  in range(1, len(str1)):
        if re.compile('[a-z]').match(str1[i - 1]) and re.compile('[a-z]').match(str1[i]):
            a.append(str1[i - 1] + str1[i])

    for  i  in range(1, len(str2)):
        if re.compile('[a-z]').match(str2[i - 1]) and re.compile('[a-z]').match(str2[i]):
            b.append(str2[i - 1] + str2[i])
    intersec = list(set(a)&set(b))
    uni_sum= 0
    for i in intersec:
        min_u = min(a.count(i), b.count(i))
        uni_sum += min_u
    intersec_sum = len(a) + len(b) - uni_sum
    if intersec_sum == 0:
        ans = 1
    else:
        print(uni_sum, intersec_sum)
        ans = uni_sum / intersec_sum

    return int(ans * 65536)

print(solution(	'aa1+aa2', "AAAA12"))


