# def solution(elements):
#     answer = set()
#     el_len = len(elements)
#     elements = elements+elements
#
#     for i in range(1,el_len+1):
#         for j in range(el_len):
#             answer.add(sum(elements[j:j+i]))
#     return len(answer)

def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

print(solution([7,9,1,1,4]))