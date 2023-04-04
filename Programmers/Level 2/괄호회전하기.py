def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        s = s[1:] + s[:1]
        for j in s:
            if len(stack) == 0:
                stack.append(j)
            else:
                if j == ")" and stack[-1] == "(":
                    stack.pop()
                elif j == "]" and stack[-1] == "[":
                    stack.pop()
                elif j == "}" and stack[-1] == "{":
                    stack.pop()
                elif j == "(" :
                    stack.append(j)
                elif j == "[" :
                    stack.append(j)
                elif j == "{" :
                    stack.append(j)
                else:
                    break

        if len(stack) == 0:
            answer += 1

    return answer




print(solution("[](){}"))