def solution(n):
    answer = 1

    if n == 1:
        return 1
    if n % 2 == 1:
        answer += 1

    for i in range(3,n,2):
        if n%i == 0:
            answer += 1     
    return answer


print(solution(1))

def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

print(expressions(15))
