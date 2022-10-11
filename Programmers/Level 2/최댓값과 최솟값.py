def solution(s):
    str_ = list(map(int, s.split()))

    print(str)

    ma = max(str_)
    mi = min(str_)

    answer = str(mi) +" "+ str(ma)
    return answer

print(solution("1 2 3 4"))