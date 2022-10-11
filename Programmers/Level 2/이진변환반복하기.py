def solution(s):
    answer = list(s)
    # 형변환 cnt, 0 개수 cnt
    tran_cnt = 0
    zero_cnt = 0
    
    #1만 남기 전까지
    while s != ['1']:
        tran_cnt += 1
        zero_cnt += s.count('0')

        # 1의 개수를 세고 cnt를 2진수로 받음
        cnt = s.count('1')
        print(cnt)
        s = list(bin(cnt)[2:])

    return [tran_cnt, zero_cnt]





print(solution("110010101001"))