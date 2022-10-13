def solution(n):
    num1 = 0
    num2 = 1
    for _ in range(n-1):
        temp = num2
        num2 = num1 + num2
        num1 = temp

        

    return num2 % 1234567

print(solution(5))