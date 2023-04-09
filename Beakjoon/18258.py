import sys
from collections import deque


cnt = int(sys.stdin.readline())
answer = deque()

for _ in range(cnt):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        answer.append(command[1])

    elif command[0] == 'pop':
        if answer:
            print(answer.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(answer))

    elif command[0] == 'empty':
        if answer:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if answer:
            print(answer[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if answer:
            print(answer[-1])
        else:
            print(-1)


