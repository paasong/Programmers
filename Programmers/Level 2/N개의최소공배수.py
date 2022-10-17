from collections import defaultdict
from os import remove


def getLem(n):
    for i in range(2, n+1):
        if n == i:
            return [i]
        elif n % i == 0 :
            return [i] + getLem(n//i)
    return 0

def solution(arr):
    if 1 in arr:
        arr.remove(1)
    num = defaultdict(int)
    answer = 1

    for a in arr:
        share = getLem(a)
        share_set = set(share)
        for i in share_set:
            if share.count(i) > num[i]:
                num[i] = share.count(i)
    
    for k, v in zip(num.keys(), num.values()):
        answer *= k**v

    return answer

#print(solution([1,2,3]))

from fractions import gcd


def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

print(nlcm([2, 3, 7, 14]));