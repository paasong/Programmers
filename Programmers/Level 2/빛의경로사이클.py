def solution(grid):
    # 아래 왼 위 오
    mx = (1, 0, -1, 0)
    my = (0, -1, 0, 1)

    lx, ly = len(grid[0]), len(grid)

    grid = [list(i) for i in grid]
    grid_check = [[[True]*4 for _ in range(lx)] for _ in range(ly)]

    answer = list()

    cnt = 0

    for y in range(ly):
        for x in range(lx):
            for i in range(4):
                if grid_check[y][x][i] == False:
                    pass
                else:
                    cnt = 0
                    nx, ny, ni = x, y, i
                    while grid_check[ny][nx][ni]:
                        grid_check[ny][nx][ni] = False
                        cnt += 1

                        if grid[ny][nx]=="S":
                            pass
                        elif grid[ny][nx] == "L":
                            ni = (ni - 1) % 4
                        elif grid[ny][nx] == "R":
                            ni = (ni + 1) % 4

                        ny = (ny + my[ni]) % ly
                        nx = (nx + mx[ni]) % lx

                    answer.append(cnt)
    answer = sorted(answer)
    return answer

print(solution(["SL","LR"]))