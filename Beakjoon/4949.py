import sys

while True:
    s = list(sys.stdin.readline())[:-1]
    answer = []
    if s == ['.']:
        break

    while s:
        pare = s.pop()
        if pare == ')' or pare == ']':
            answer.append(pare)

        elif pare == '(':
            if answer and answer[-1] == ')':
                answer.pop()
            else:
                answer.append(pare)
                break
        elif pare == '[':
            if answer and answer[-1] == ']':
                answer.pop()
            else:
                answer.append(pare)
                break
    if answer == []:
        print('yes')
    else:
        print('no')

