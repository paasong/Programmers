def solution(d, budget):
    d.sort()
    sum = 0
    b = list()
    for i in d:
        sum += i
        if sum <= budget:
            b.append(i)

    return len(b)