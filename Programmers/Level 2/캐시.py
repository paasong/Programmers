# def solution(cacheSize, cities):
#     cache = list()
#     answer = 0
#     while cities:
#         city = cities.pop(0)
#         city = city.lower()
#
#
#         if city in cache:
#             answer += 1
#             cache.remove(cache.index(city))
#            #cache.remove(city)
#         else:
#             answer += 5
#         cache.append(city)
#         if len(cache) > cacheSize:
#             cache.pop(0)
#
#     return answer

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    print(cache)
    time = 0

    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))