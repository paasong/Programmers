def solution(clothes):
    clothes_dict = dict()
    ans = 0

    for i in clothes:
        if i[1] not in clothes_dict.keys():
            clothes_dict[i[1]] = list()
            clothes_dict[i[1]].append(i[0])
        else:
            clothes_dict[i[1]].append(i[0])

    for i in clothes_dict:
        cnt_clothes = len(clothes_dict[i])
        ans += ans * cnt_clothes + cnt_clothes


    return ans

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))