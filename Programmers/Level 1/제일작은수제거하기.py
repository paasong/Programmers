def solution(arr):
    arr.remove(min(arr))
    if arr != []:
        return arr
    else:
        return [-1]


print(solution([2]))