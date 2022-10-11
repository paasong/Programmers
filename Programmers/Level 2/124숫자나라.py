def solution(n):
    match = {0:3, 1:1, 2:2}
    str_124 = {0:'4', 1:'1', 2:'2'}
    remainder = 0
    result= ''

    while n > 0:
        remainder = n % 3
        n = (n - match[remainder]) / 3
        result = str_124[remainder]+result

    return result



print(solution(13))

