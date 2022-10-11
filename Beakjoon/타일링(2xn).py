width = int(input())

cache = [0]*1001

cache[1] = 1
cache[2] = 2

for i in range(3, len(cache)):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[width]%10007)