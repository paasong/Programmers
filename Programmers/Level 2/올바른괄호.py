def solution(s):
    stack_s = list()

    for i in s:
        if len(stack_s) == 0:
            stack_s.append(i)

        elif i == ')' and stack_s.pop() == '(':
            pass
        else:
            stack_s.append(i)

            pass

    print(stack_s)
    if len(stack_s) == 0:
        return True
    else:
        return False