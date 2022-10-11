def solution(numbers):
    sum1 = 45
    #for i in set(numbers):
    sum1 -= sum(set(numbers))

    return sum1

print(solution([1,2,3,4,6,7,8,0]))

a, b = map(int, input().strip().split(' '))
print(a + b)