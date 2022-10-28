def solution(n,a,b):
    for i in range(1, 20):
        if 2**i == n:
            cnt = i
            break
    
    a, b = min([a, b]), max([a, b])

    for _ in range(cnt):
        if 

print(solution(8, 4, 7))