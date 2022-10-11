import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    arr3 = arr1 @ arr2
    arr3 = arr3.tolist()

    return arr3

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))