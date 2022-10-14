def solution(brown, yellow):

    for i in range(1, yellow+1):
        if yellow % i == 0:
            h = yellow // i
            w = i

            if (h*2) + (w*2) + 4 == brown:
                return [h+2, w+2]
    return 0


print(solution(24,24))