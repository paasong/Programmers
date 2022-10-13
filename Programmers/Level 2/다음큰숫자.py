def solution(n):
    bin_n = list(bin(n)[2:])
    len_n = len(bin_n)


    for i in range(len_n-1, 0, -1):
        if bin_n[i] == '1' and bin_n[i-1] == '0':
            if i == len_n - 1:
                bin_n[i], bin_n[i-1] = bin_n[i-1], bin_n[i]
                answer = '0b'+''.join(bin_n)
                return int(answer,2)
            else:
                bin_n[i], bin_n[i-1] = bin_n[i-1], bin_n[i]
                answer = '0b'+''.join(bin_n[:i] + sorted(bin_n[i:]))
                return int(answer,2)
        elif i == 1:
            answer = '0b'+''.join(['1','0'] + sorted(bin_n[i:]))
            return int(answer,2)
    return 0

def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n

print(solution(78))
print(nextBigNumber(78))