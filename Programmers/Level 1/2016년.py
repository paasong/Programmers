def solution(a, b):
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_week = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE','WED']
    sum_day = 0
    if a == 1:
        sum_day = b
    else:
        sum_day = sum(day_list[:a-1],b)
    answer = day_week[sum_day % 7]


    return answer

print(solution(5,24))