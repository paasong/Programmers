def solution(w,h):
    num = 1
    for i in range(min(w, h),0,-1):
        if w % i == 0 and h % i == 0:
            num = i
            break

    w_m = w / num
    h_m = h / num

    m = min(w_m, h_m)

    if w_m == h_m:
        return w * h - num
    else:
        return w * h - (m * 2 * num)

    return 0

print(solution(9, 8))