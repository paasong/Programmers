def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = []
    period = 0
    row, col = len(maps), len(maps[0])
    print(row, col)
    visited = [[True]*col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and visited[i][j]:
                need_visit = [(i, j)]
                period = 0

                while need_visit:
                    print('need_visit',need_visit)
                    x, y = need_visit.pop(0)
                    if visited[x][y]:
                        period += int(maps[x][y])
                        visited[x][y] = False
                        for k in range(len(dx)):
                            mx, my = x+dx[k], y+dy[k]
                            if (-1 < mx < row) and (-1 < my < col):
                                if  maps[mx][my] != 'X' and visited[mx][my]:
                                    need_visit.append((mx, my))

                answer.append(period)
    answer.sort()
    if answer == list():
        return [-1]
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))