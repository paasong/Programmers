n, m = map(int, input().split())

s = [] # 조합의 배열을 넣음
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    print('----------------------')
    print(s)
    f()
    print('======================')
    print(s)
    s.pop()

f()

#
# n, m = map(int, input().split())
# s = []
#
# for i in range(1, n+1):
#
#
# if len(s) == m:
#   print(' '.join(map(str,s)))



