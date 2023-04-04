def solution(n, left, right):
    s = left // n
    e = right // n

    a_list= list()
    base_list = [i+1 for i in range(n)]

    for i in range(s, e+1):
        a = base_list.copy()
        a[0:i+1] = [i+1 for _ in range(i+1)]
        a_list += a
    print(a_list)
    answer = a_list[left-(n*s) : right-(n*s)+1]
    return answer

# def solution(n, left, right):
#     answer = []
#     for i in range(left,right+1):
#         print(max(i//n,i%n)+1)
#         answer.append(max(i//n,i%n)+1)
#     return answer

print(solution(4,7,14))