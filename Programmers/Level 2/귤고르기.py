def solution(k, tangerine):
    answer = 0
    cnt = 0

    tan_dict = dict()

    for i in tangerine:
        if tan_dict.get(i) == None:
            tan_dict[i] = 1
        else:
            tan_dict[i] += 1

    tan_cnt = sorted(tan_dict.items(), key=lambda x: x[1], reverse=True)

    for (i, j) in tan_cnt:
        if answer < k:
            answer += j
            cnt += 1
        else:
            break
    return cnt