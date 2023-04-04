# def solution(priorities, location):
#     print_list = list()
#     print_temp = list()
#     answer = 0
#     for i in range(len(priorities)):
#         print_list.append((i, priorities[i]))
#
#     #print(print_list)
#     for i in range(len(priorities)):
#         pri = max(print_list, key=lambda x: x[1])[1]
#         #print(pri)
#         for _ in range(len(priorities)):
#             #print('print_list[0][1]',print_list[0][1])
#             if print_list[0][1] == pri:
#                 pri_pop = print_list.pop(0)
#                 answer += 1
#                 if pri_pop[0] == location:
#                     return answer
#
#                 break
#             else:
#                 pri_pop = print_list.pop(0)
#                 print_temp.append(pri_pop)
#         #print('print_temp',print_temp)
#         print_list = print_list+print_temp
#         print_temp = list()
#         #print(print_list)
#
#     return answer

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print('queue',queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        print('cur',cur)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer



print(solution([2, 1, 3, 2], 1))