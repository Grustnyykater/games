def is_enter_ok(y, x):
    if not y.isdigit() or not x.isdigit():  # Если x или y - не цифры, то возвращаем ложь
        return False
    if not (1 <= int(y) <= 4) or not (
            1 <= int(x) <= 5):  # если x или y выходят за пределы индексации поля, возвращаем ложь
        return False
    if field[int(y) - 1][int(x) - 1] != '.':
        return False
    return True


def display_field():
    print("  ", '1', '2', '3', '4', '5')
    print(" ", ' -' * 5)
    print('1|', field[0][0], field[0][1], field[0][2], field[0][3], field[0][4])
    print('2|', field[1][0], field[1][1], field[1][2], field[1][3], field[1][4])
    print('3|', field[2][0], field[2][1], field[2][2], field[2][3], field[2][4])
    print('4|', field[3][0], field[3][1], field[3][2], field[3][3], field[3][4])


def end_of_the_game():  # проверяем игру на окончание
    if '.' not in field[0] and '.' not in field[1] and '.' not in field[2] and '.' not in field[
        3]:  # если не осталось пустых клеток, то игра окончена
        return True
    return False


def check(ny, nx):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)] # проверим все клетки в окрестности
    for dy, dx in moves:
        dy1 = dy + ny
        dx1 = dx + nx
        if 0 <= dy1 <= 3 and 0 <= dx1 <= 4: # важно чтобы координаты не вышли за границы массива
            if field[ny][nx] == field[dy1][dx1]: # если клетка из окрестности равна клетки в которую игрок поставил свой символ
                score[h % 3] += 1 # начисляем штрафное очко


field = []
for i in range(4):  # создаем поле
    m = ["."] * 5
    field.append(m)

h = 0  # Заведем переменную, для ходов
score = [0, 0, 0]  # и список с счетом для каждого игрока

while True:
    display_field()
    print("Текущий счет:", score[0], score[1], score[2])
    print("Ход игрока: ", h % 3 + 1, "Введите координаты, куда поставите свой символ(на разных строках)")
    print("Сначала по вертикали, затем по горизонтали")
    inp1 = input()
    inp2 = input()
    if not is_enter_ok(inp1, inp2):
        print("Неверный ввод. Попробуйте еще раз.")
        continue
    y, x = int(inp1) - 1, int(inp2) - 1  # приводим введеные координату к типу <int>
    field[y][x] = str(h % 3 + 1)  # по введенным координатам заполняем ячейку символом игрока
    check(y, x)
    if end_of_the_game():
        print("Игра окончена!")
        display_field()
        print("Текущий счет:", score[0], score[1], score[2])
        print("Победил игрок", score.index(min(score)) + 1)
        break
    h += 1
