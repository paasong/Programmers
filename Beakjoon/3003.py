pieces = [1,1,2,2,2,8]
a = map(int, input().split())
for i, j in zip(pieces, a):
    print(i-int(j), end=' ')