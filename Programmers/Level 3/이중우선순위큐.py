def solution(operations):
    oper_list = list()
    for oper in operations:
        a = oper.split(' ')

        if a[0] == 'I':
            oper_list.append(int(a[1]))
        else:
            if oper_list:
                oper_list.sort()
                if int(a[1]) < 0:
                    oper_list.pop(0)
                else:
                    oper_list.pop(-1)

    if oper_list == []:
        oper_list = [0]
    oper_list.sort()
    return [oper_list[-1],oper_list[0]]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))