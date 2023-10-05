import random


def print_board(board):
    for row in board:
        print(" ".join(row))


def check_win(board):
    for i in board:
        if "0" in i:
            return False
    return True


moves = ["a", "b", "c", "d", "e", "f", "g", "h"]
movesLn = ["8", "7", "6", "5", "4", "3", "2", "1"]

""" 
# - пустые поля 
0 - пуговицы 
"""

board = [[random.choice(["#", "0"]) for i in range(8)] for j in range(8)]
name1 = input("Первый игрок, введите свое имя: ")
name2 = input("Второй игрок, введите свое имя: ")

k = 1

# Когда ходит первый - ноу_мув = Тру. Когда второй - Фолз

while True:

    print_board(board)

    if check_win(board) == True:
        winner = ""
        if k % 2 == 0:
            winner = name1
        else:
            winner = name2
        print("Конец игры. Победа: ", winner)
        break

    if k % 2 != 0:

        print(name1, ", напишите номер строки(сверху вниз от 8 до 1) или букву столбца(cлева направо от a до h):")
        move = input("Ход: ")

        if move in moves:
            stolbik_index = moves.index(move)
            for i in range(len(board)):
                if board[i][stolbik_index] == "0":
                    board[i][stolbik_index] = "#"

        elif move in movesLn:
            line_index = movesLn.index(move)
            if "0" in board[line_index]:
                board[line_index] = ["#" for i in range(8)]
        else:
            print("Некорректный ввод")
            break
        k += 1
    elif k % 2 == 0:
        print(name2, ", напишите номер строки(сверху вниз от 8 до 1) или букву столбца(cлева направо от a до h):")
        move = input("Ход: ")
        if move in moves:
            stolbik_index = moves.index(move)
            for i in range(len(board)):
                if board[i][stolbik_index] == "0":
                    board[i][stolbik_index] = "#"

        elif move in movesLn:
            line_index = movesLn.index(move)
            if "0" in board[line_index]:
                board[line_index] = ["#" for i in range(8)]
        else:
            print("Некорректный ввод")
            break
        k += 1
    else:
        print("Неизвестная ошибка")