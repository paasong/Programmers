def solution(arr):
    a = arr[0]
    answer = []
    for i in arr :
        if a != i :
            answer.append(a)
        a = i
    answer.append(arr[-1])
    return  answer

print(solution([1,1,3,3,0,1,1]))