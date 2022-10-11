from itertools import combinations

def check(places, com_pla):
    for i in com_pla:
        try:
            if (abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])) == 1:
                return 0
            if (abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])) == 2:
                if i[0][0] == i[1][0]:
                    if places[i[0][0]][i[0][1] + 1] == 'O':
                        return 0

                if i[0][1] == i[1][1]:
                    if places[i[0][0] + 1][i[0][1]] == 'O':
                        return 0
                if i[0][0] + 1 == i[1][0] and i[0][1] -1 == i[1][1]:
                    if places[i[0][0]][i[0][1] - 1] == 'O' or places[i[0][0] + 1][i[0][1]] == 'O':
                        return 0
                elif i[0][0] + 1 == i[1][0] and i[0][1] + 1 == i[1][1]:
                    if places[i[0][0]][i[0][1] + 1] == 'O' or places[i[0][0] + 1][i[0][1]] == 'O':
                        return 0
        except:
            pass
    return 1

def solution(places):
    answer = list()
    for places in places:
        P_pla = list()
        place = [j for j in places]

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    P_pla.append([i,j])


        com_pla = list(combinations(P_pla,2))
        answer.append(check(places, com_pla))

    return answer

print(solution([["XXPXX", "XXOXX", "XXPXX", "XXXXX", "XXXXX"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))