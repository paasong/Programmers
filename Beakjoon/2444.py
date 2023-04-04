# step = int(input())-1
# step_s = step
# star = 1
# print(' '* step_s, '*' * star, sep='')
#
# for _ in range(step):
#     step_s -= 1
#     star += 2
#     print(' ' * step_s, '*' * star, sep='')
#
# for _ in range(step):
#     step_s+=1
#     star -= 2
#     print(' ' * step_s, '*' * star, sep='')

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * ((2 * i - 1)))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1))