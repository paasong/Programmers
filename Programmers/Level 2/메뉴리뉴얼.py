from itertools import combinations
from collections import Counter


def solution2(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            com = combinations(sorted(order), c)
            temp += com
        print('temp',temp)
        cnt = Counter(temp)

        if len(cnt) != 0 and max(cnt.values()) != 1:
            answer += [''.join(f) for f in cnt if cnt[f] == max(cnt.values())]

    return sorted(answer)


print(solution2(["ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE"], [2,3,5]))
