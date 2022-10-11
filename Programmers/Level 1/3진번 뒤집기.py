def solution(n):
    remainder = 0
    to_3 = list()
    sum = 0
    while n > 0:
        remainder = n % 3
        n = n//3
        to_3.append(remainder)
    for num, i in enumerate(to_3[-1::-1]):
        sum += (i * (3**num))

    return sum

print(solution(125))