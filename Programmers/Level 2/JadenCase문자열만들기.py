def solution(s):
    s = s.lower()
    s = list(s)
    s[0] = s[0].upper()
    for i, j in zip(range(len(s)),range(1, len(s))):
        if s[i] == " ":
            s[j] = s[j].upper()

    answer = ''.join(s)
    return answer

solution("people unFollowed me")