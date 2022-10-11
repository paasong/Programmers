def solution(array, commands):
    answer = []

    for i in commands:
        new_arr = array[i[0]-1:i[1]]
        new_arr.sort()
        num = new_arr[i[2]-1]
        answer.append(num)

    return answer