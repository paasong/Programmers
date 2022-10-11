import re
def solution(s):
    answer = ''
    num_table={'zero': '0',
               'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}

    sum_i = ''
    for i in s:
        sum_i += i
        if sum_i in num_table:
            answer += num_table[sum_i]
            sum_i = ''
        elif i in num_table.values() :
            answer += i
            sum_i = ''

    return int(answer)

print(solution('23four5six7'))