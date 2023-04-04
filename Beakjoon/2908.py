# num = list(map(str,input().split()))
# ans = ['' for _ in range(2)]
#
# for idx in range(2,-1,-1) :
#     ans[0] += num[0][idx]
#     ans[1] += num[1][idx]
#
# print(max(int(ans[0]), int(ans[1])))

a, b = input().split()
a = a[::-1]
b = b[::-1]
print(max(a, b))