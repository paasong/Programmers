import math
def solution(n,a,b):
    if a > b:
        a, b = b, a
    return search(n,a,b,0,n)

def search(n, a, b, start, end):
    answer = math.log(n, 2)
    n = n / 2
    m = (start + end) / 2

    if a <= m and b > m:
        return int(answer)
    elif a < m and b <= m:
        return search(n, a, b, start, m)
    else:
        return search(n, a, b, m, end)



print('solution',solution(8, 5, 6))