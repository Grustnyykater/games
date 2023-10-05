# Создаем пустое поле для игры
board = ['.' for _ in range(9)]


# Функция для отображения игрового поля
def display_board():
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('|', board[6], '|', board[7], '|', board[8], '|')


# Функция для хода игрока
def make_move(player):
    while True:
        print("Игрок", player)
        position = input("Выберите позицию для хода (от 1 до 9): ")
        if position.isdigit() is False:  # Проверяем, что пользователь ввел число
            print("Неверный ввод! Попробуйте еще раз.")
            continue  # Если введено не число, даем ввести число еще раз
        position = int(
            position) - 1  # Преобразуем введеное число из <str> в <int> и отнимаем единицу, так как индексация в массиве начинается с 0
        if not (0 <= position <= 8):
            print("Введите число из корректного диапазона!")
            continue
        if board[position] != '.':
            print('Эта клетка уже занята! Попробуйте еще раз.')
            continue
        if position >= 0 and position <= 8 and board[position] == '.':
            board[position] = player  # заменяем пустую строку в нашем массиве на символ текущего игрока
            break


# Функция для проверки победителя
def check_winner():
    if board[0] == board[1] == board[2] != '.' or board[3] == board[4] == board[5] != '.' or board[6] == board[7] == board[8] != '.':  # проверяем горизонтальные комбинации
        return True
    if board[0] == board[3] == board[6] != '.' or board[1] == board[4] == board[7] != '.' or board[2] == board[5] == board[8] != '.':  # вертикальные комбинации
        return True
    if board[0] == board[4] == board[8] != '.' or board[2] == board[4] == board[6] != '.':  # диагональные комбинации
        return True
    return False  # Иначе возвращаем ложь


current_player = 'X'
print("Индексация в игровом поле имееет следующий вид:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print()
while True:  # Основной игровой цикл
    display_board()  # Печатаем игровое поле
    make_move(current_player)  # В функцию make_move передаем символ текущего игрока
    if check_winner():  # Проверяем, завершилась ли игра, или можно ходить дальше
        display_board()
        print("Игрок", current_player, "победил!")
        break
    if '.' not in board:
        display_board()
        print("Ничья!")
        break
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'
