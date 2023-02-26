#230226 7682 틱택토
# 주어진 상태가 게임의 승패가 결정난 최종 상태인지 출력하라.

import sys

input = sys.stdin.readline

result = set()
board = ["."]*9
madeIdxs = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def backtrack(turn):
    global board, result,madeIdxs

    for madeIdx in madeIdxs:
        made = "".join([board[madeIdx[0]],board[madeIdx[1]],board[madeIdx[2]]])
        if made == "OOO" or made == "XXX":
            result.add("".join(board))
            return

    allCheck = True

    for idx in range(9):
        if board[idx] == ".":
            allCheck = False
            board[idx] = "O" if turn else "X"
            if "".join(board) not in result:
                backtrack(1 - turn)
            board[idx] = "."

    if allCheck:
        result.add("".join(board))
    return

backtrack(0)
while 1:
    getStr = input().rstrip()
    if getStr == "end":
        break

    if getStr in result:
        print("valid")
    else:
        print("invalid")
