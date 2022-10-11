def solution(nums):
    # num_len = len(nums)
    # nums = set(nums)
    #
    # if len(nums) >= num_len//2 :
    #     return num_len//2
    # else:
    #     return len(nums)
    #
    # return None
    return min(len(nums)//2, len(set(nums)))

print(solution([3,1,2,3]))