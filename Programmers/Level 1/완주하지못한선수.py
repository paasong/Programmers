def solution(participant, completion):

    participant.sort()
    completion.sort()
    count = 0

    for p , c in zip(participant, completion):
        if p != c :
            return p
    return participant.pop()

print(solution(	["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))