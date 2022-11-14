def solution(triangle):
    result = triangle[0]
    for i in triangle[1:]:
        i_len = len(i)
        # i = 3, 8
        a = list()
        for k in range(len(i)):
            if k == 0:
                a.append(i[k]+result[k])
            elif k == i_len-1:
                a.append(i[k] + result[k-1])
            else:
                max_num = max(i[k]+result[k-1], i[k] + result[k])
                a.append(max_num)
        result = a

    return max(result)

#print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(solution([[7], [3, 8], [8, 1, 0]]))