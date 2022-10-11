def solution(n, arr1, arr2):
    remainder1 = 0
    remainder2 = 0


    answer =list()

    for num1, num2 in zip(arr1, arr2):
        restr = ''
        for i in range(n):
            remainder1, remainder2 = num1 % 2, num2 % 2
            num1, num2 = num1 // 2 , num2 //2
            if remainder1 == 0 and remainder2 == 0 :
                restr = ' ' + restr
            else:
                restr = '#' + restr

        answer.append(restr)



    return answer

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))