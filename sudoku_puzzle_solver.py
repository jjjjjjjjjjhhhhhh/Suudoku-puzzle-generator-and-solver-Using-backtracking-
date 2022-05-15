import numpy as np

def possible(rows, column, number):
    global board

    for i in range(0, 9):
        if board[rows][i] == number:
            return False

    for i in range(0, 9):
        if board[i][column] == number:
            return False
          
    x0 = (column // 3) * 3
    y0 = (rows // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0+i][x0+j] == number:
                return False



    return True

def solve():
    global board
    for rows in range(0, 9):
        for column in range(0, 9):
            if board[rows][column] == 0:
                for number in range(1, 10):
                    if possible(rows, column, number):
                        board[rows][column] = number
                        solve()
                        board[rows][column] = 0

                return
