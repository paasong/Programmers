def solution(cacheSize, cities):
    cache = list()
    answer = 0
    while cities:
        city = cities.pop(0)
        city = city.lower()


        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
        else:
            answer += 5
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)

    return answer

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))