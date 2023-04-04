# def solution(picks, minerals):
#     answer = 0
#     minerals_cnt = []
#     minerals = minerals[:(sum(picks))*5]
#
#     for i in range(len(minerals)//5+1):
#         dia, iron, stone = minerals[i*5:i*5+5].count('diamond'),minerals[i*5:i*5+5].count('iron'),minerals[i*5:i*5+5].count('stone')
#         minerals_cnt.append([dia, iron, stone])
#     minerals_cnt.sort(key=lambda x:(x[0],x[1]), reverse= True)
#
#     for i, p in enumerate(picks):
#         for j in range(p):
#             mi = minerals_cnt.pop(0)
#             if i == 0:
#                 answer += mi[0]
#                 answer += mi[1]
#                 answer += mi[2]
#             elif i == 1:
#                 answer += mi[0]*5
#                 answer += mi[1]
#                 answer += mi[2]
#             elif i == 2:
#                 answer += mi[0]*25
#                 answer += mi[1]*5
#                 answer += mi[2]
#             if minerals_cnt == []:
#                 return  answer
#
#     return answer

def solution(picks, minerals):
    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1},)):
            if picks[i] > 0:
                temp_picks = picks.copy()
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5])))
        return min(result)

    return solve(picks, minerals, 0)

print(solution([1,3,2],	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))