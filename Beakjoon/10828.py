# loop = int(input())
# stack_list = []
# for _ in range(loop):
#     command = list(map(str,input().split()))
#     if command[0] =='push':
#         stack_list.append(command[1])
#     elif command[0] == 'pop':
#         if stack_list == []:
#             print(-1)
#         else:
#             print(stack_list[-1])
#             del stack_list[-1]
#     elif command[0] == 'size':
#         print(len(stack_list))
#     elif command[0] == 'empty':
#         if stack_list :
#             print(0)
#         else:
#             print(1)
#     elif command[0] == 'top':
#         if stack_list:
#             print(stack_list[-1])
#         else:
#             print(-1)

loop = int(input())
stack_list = []
for _ in range(loop):
    command = list(map(str,input().split()))
    if command[0] =='push':
        stack_list.append(command[1])
    elif command[0] == 'pop':
        if stack_list == []:
            print(-1)
        else:
            print(stack_list[-1])
            del stack_list[-1]
    elif command[0] == 'size':
        print(len(stack_list))
    elif command[0] == 'empty':
        if stack_list :
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if stack_list:
            print(stack_list[-1])
        else:
            print(-1)