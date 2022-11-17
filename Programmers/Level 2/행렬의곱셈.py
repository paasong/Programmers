import numpy as np

def solution(arr1, arr2):
    answer = np.array(arr1)@np.array(arr2)
    return answer.tolist()

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))