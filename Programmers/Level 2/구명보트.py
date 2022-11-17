def solution(people, limit):
    people.sort()
    ans = 0
    a, b = 0, len(people)-1

    while a <= b:
        if people[a] + people[b] <= limit:
            a += 1
        b -= 1
        ans += 1
    return ans

print(solution([70, 50, 80, 50], 100))