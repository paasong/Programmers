def solution(arr):
    answer = []
    answer.append(arr[0])

    for i, j in zip(arr, arr[1:]):
        if i != j:
            answer.append(j)
        else:
            pass
    return answer