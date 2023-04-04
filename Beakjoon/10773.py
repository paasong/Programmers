import sys

loop = int(sys.stdin.readline())
cal = list()

for _ in range(loop):
    num = int(sys.stdin.readline())
    if num == 0:
        cal.pop()
    else:
        cal.append(num)

print(sum(cal))
