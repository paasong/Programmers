def solution(N, stages):
    stages.sort()
    sta_num = len(stages)
    fail_rate = dict()
    result = []

    for i in range(1,N+1):
        print(i)
        num = stages.count(i)
        fail_rate[num / sta_num] = list()
        sta_num -= num

        if sta_num == 0:
           sta_num = 1

    print(fail_rate)
    sta_num = len(stages)

    for i in range(1,N+1):
        num = stages.count(i)
        fail_rate[num / sta_num].append(i)
        sta_num -= num
        if sta_num == 0:
           sta_num = 1


    print(fail_rate)


    fk = list(fail_rate.keys())
    fk.sort(reverse=True)
    for i in fk:
        result.extend(fail_rate[i])


    print(fk)

    return result


print(solution(5,[2,2,2,2,2]))
