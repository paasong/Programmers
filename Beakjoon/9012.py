import sys

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    ps = list(sys.stdin.readline())[:-1]
    check = 0
    while ps :
        p = ps.pop()

        if p == '(' and check ==0 :
            check = -1
            break

        if p == ')':
            check += 1
        else:
            check -= 1

    if check == 0:
        print("YES")
    else:
        print("NO")