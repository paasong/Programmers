import math

def solution(progresses, speeds):
    check = True
    cnt = 1
    result = []
    day_pred = math.ceil((100 - progresses[0]) / speeds[0])

    for progres, speed in zip (progresses[1:],speeds[1:]):
        print('count')
        check = True
        day_next = math.ceil((100 - progres) / speed)
        if day_pred >= day_next:
            cnt += 1
        else:
            day_pred = day_next
            result.append(cnt)
            check = False
            cnt = 1


    result.append(cnt)
    return result
print(solution( [99, 99, 99, 99, 99], [99, 99, 99, 99, 99]))