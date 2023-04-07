import sys
n = int(input())
cnt = 1
stack = []
ans = []
for i in range(n):
    num = int(sys.stdin.readline())
    while cnt<=num: #cnt 스택에 push
        stack.append(cnt)
        ans.append('+')
        cnt+=1
        #print(ans)
    if stack.pop()==num: #stack의
        ans.append('-')
        #print(ans)
    else:
        print("NO")
        break
else:
    print("\n".join(ans))


# import sys
# cnt = int(sys.stdin.readline())
# len_max = 1
# sequence = []
# answer = []
# for _ in range(cnt):
#     num = int(sys.stdin.readline())
#     sequence += [i for i in range(len_max,num+1)]
#     answer += ['+' for _ in range(len_max,num+1)]
#     if sequence.pop() != num:
#         break
#     answer += ['-']
#     if len_max <= num:
#         len_max = num+1
# if sequence:
#     print('NO')
# else:
#     print('\n'.join(answer))