def calculate(odd_num, even_num):
    a = even_num // odd_num
    b = even_num % odd_num

    return odd_num * (a + 1) + (b - 1)


def solution(w,h):
    num = 0
    answer = 1
    gcd = 0
    # 같은 경우

    if w == h:
        return w * w - w



    s, b = min(w, h), max(w, h)
    print(b/2)
    for i in range(1, b // 2 + 1) :
        if s % i == 0 and b % i == 0:
            gcd = i

    s /= gcd
    b /= gcd

    #홀짝
    if s % 2 == 0 :
        num = calculate(b, s)

    elif s % 2 == 1 :
        num = calculate(s, b)


    return int(w * h - (num * gcd))


print(solution(10,5))
