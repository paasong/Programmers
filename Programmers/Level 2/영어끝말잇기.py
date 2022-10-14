def solution(n, words):
    eng = dict()


    for i in range(len(words)):
        if  words[i-1][-1]!= words[i][0] and i != 0:
            print(words[i-1], words[i])
            print(words[i-1][-1], words[i][0])
            print(i)
            return [(i%n)+1, (i//n)+1]

        if eng.get(words[i][0]) is None:
            eng[words[i][0]] = [words[i]]

        else:
            if words[i] not in eng[words[i][0]]:
                eng[words[i][0]].append(words[i] )
            else:
                return [(i%n)+1, (i//n)+1]

    return [0, 0]


print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))