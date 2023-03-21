def solution(beginning, target):
    board_height = len(beginning)
    board_length = len(beginning[0])

    # 안뒤집어도 되는 칸은 0, 뒤집어야 하는 칸은 1
    board = [[0 if beginning[i][j] == target[i][j] else 1 for j in range(board_length)] for i in range(board_height)]

    print(board)
    # column 정의
    col = lambda num: [board[i][num] for i in range(board_height)]

    # 가로줄 확인
    for row in board:
        if row not in (board[0], [0 if board[0][i] == 1 else 1 for i in range(board_length)]):
            return -1

    # 세로줄 확인
    for column in [col(i) for i in range(board_length)]:
        if column not in (col(0), [0 if col(0)[i] == 1 else 1 for i in range(board_height)]):
            return -1

    # 세로로 뒤집는 횟수 + 가로로 뒤집는 횟수
    if board[0].count(1) > board_length/2 and board[0].count(1) > col(0).count(1):
        return board[0].count(0) + col(0).count(1 if board[0][0] == 1 else 0)
    else:
        return board[0].count(1) + col(0).count(0 if board[0][0] == 1 else 1)


# print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
#
# print(solution([[0, 1, 1],[1, 0, 0],[1, 0, 0]],[[0, 0, 0],[0, 0, 0],[0, 0, 0]]))
# print(solution([[1, 1, 1],[0, 0, 0],[0, 0, 0]],[[0, 0, 0],[0, 0, 0],[0, 0, 0]]))
print(solution([[1, 0, 0],[1, 0, 0],[0, 1, 1]],[[0, 0, 0],[0, 0, 0],[0, 0, 0]]))
