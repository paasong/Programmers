def solution_1(n, cores):
    start, end = 0, 10000#max(cores)*n
    cnt, m = 0, 0
    answer =0
    if n <= len(cores):
        return n
    while start+1 < end :
        cnt = 0
        m = (start + end) // 2
        for i in cores:
            cnt += ((m//i) + 1)

        if cnt < n:
            start = m
        else:
            end = m
    if n <= cnt:
        cnt = 0
        m = m-1
        for i in cores:
            cnt += ((m//i) + 1)
    capacity = n-cnt
    for i, c in enumerate(cores,1):

        if (m+1) % c == 0:
            capacity -= 1
            if capacity == 0:
                return i
    return answer

# def solution(n, cores):
#     remain = [0 for _ in cores]
#     print('main',remain)
#     while n:
#         for i in range(len(cores)):
#             if remain[i] == 0:
#                 n-=1
#                 if n == 0: return i+1
#                 remain[i] += cores[i]
#         remain = list(map(lambda x: x-1, remain))
#         print(remain)


print( solution(9, [1,2,3]))