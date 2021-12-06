# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict


def build_bord(raw_board):
    board = []
    for b in raw_board:
        board.append([int(b[i:i + 3]) for i in range(0, len(b), 3)])
    return board


def build_boards(boards):
    i = 1
    while i < len(boards) - 6:
        yield build_bord(boards[i:i + 5])
        i += 6


def hasWin(board, row_index, column_index):
    if all(map(lambda v: v == '-', board[row_index])):
        return True
    in_column = True
    for r in board:
        in_column = in_column and r[column_index] == '-'
    if in_column:
        return True


def compute(board, n):
    sum = 0
    for r in board:
        for c in r:
            sum += c if c != "-" else 0
    print(sum * n)


def replace(n, board):
    for i, r in enumerate(board):
        try:
            found = r.index(n)
            if found >= 0:
                r[found] = '-'
                if hasWin(board, i, found):
                    compute(board, n)
                    return True
        except ValueError:
            continue
    return False


board_done = []


def replace_for_all(n, boards):
    for i, b in enumerate(boards):
        if i in board_done:
            continue
        if replace(n, b):
            board_done.append(i)


def print_hi():
    with open('bingo_board.txt') as f:
        boards = f.readlines()
    numbers = boards[0][:-1].split(',')
    print(numbers)

    boards = list(build_boards(boards[1:]))
    for n in numbers:
        replace_for_all(int(n), boards)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
