from sys import stdin, stdout

cnt_num1 = int(stdin.readline())
num_list = sorted(map(int,stdin.readline().split()))

cnt_num2 = stdin.readline()
find_list = map(int, stdin.readline().split())



def search_num(num_list, find_num, start, end):
    median_num = (start + end) //2

    if start >= end:
        return 0
    elif num_list[median_num] < find_num:
        return search_num(num_list, find_num, median_num+1, end)

    elif num_list[median_num] > find_num:
        return search_num(num_list, find_num, start, median_num)
    else:
        return 1


for i in find_list:
    print(search_num(num_list, i, 0, cnt_num1))
