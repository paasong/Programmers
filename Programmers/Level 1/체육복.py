def solution(n, lost, reserve):
    n = n - len(lost)

    l = lost.copy()

    for i in l:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            n += 1

    lost.sort()


    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            n += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            n += 1

    return  n
print(solution(5, [5,4,2] , [2,4]))
#2, [2], [1]
#4