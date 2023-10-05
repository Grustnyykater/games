import random


def print_board(board):  # вывод игрового поля
    for row in board:
        print(row)


def make_move(board, player_sum, row, col):  # делаем ход
    if row < 0 or row > 2 or col < 0 or col > 2:  # проверка на корректность ввода
        print("Неверный ход. Выбери значения от 1 to 3.")
        return board, player_sum

    num = board[row][col]
    board[row][col] = 0

    player_sum += num

    return board, player_sum


def check_game_over(board):  # проверка на окончание игры
    for row in board:
        for num in row:
            if num != 0:  # пока не останутся все нули. Если хотя бы один не ноль - игра не окончена
                return False
    return True


def get_winner(player1_sum, player2_sum):  # Результат игры
    if player1_sum > player2_sum:
        return "Игрок 1 побеждает!"
    elif player1_sum < player2_sum:
        return "Игрок 2 побеждает!"
    else:
        return "Ничья!"


# Создание игрового поля
board = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
player1_sum = 0
player2_sum = 0

# Вывод игрового поля
print_board(board)

while not check_game_over(board):  # основной игровой цикл
    row = int(input("Введи ряд от 1 до 3: "))
    col = int(input("Введи столбец от 1 до 3: "))
    # отнимаем от номеров 1 тк индексы с 0
    row = row - 1
    col = col - 1

    board, player_sum = make_move(board, player1_sum, row, col)  # делаем ход

    # Переключение между игроками
    if player1_sum == 0:
        player1_sum = player_sum
        player_sum = 0
    else:
        player2_sum = player_sum
        player_sum = 0

    # Вывод игрового поля
    print_board(board)

print(get_winner(player1_sum, player2_sum))  # запускаем проверку победителя и выводим результат