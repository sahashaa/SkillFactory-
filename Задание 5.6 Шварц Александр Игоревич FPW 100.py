gamezone=[[' ']*3 for i in range(3)]#Создание игрового поля
def monic():  ##Интерфейс
    print(f'   0  1  2 ')
    for i in range(3):
        print(f' {i}   {"-".join(gamezone[i]) }')  #используем функцию джоин чтобы перевести все в кортеж
        #Я так и не смог понять почему дефис появляется только в 2 и 3 столбике

def move():  #Ввод пользователя
    while True:
        dots = tuple(map(int, input('Твоя очередь:').split()))  #мапим список для приведения всех символов к числам,и переводим обратно в кортеж для того чтобы функция len работала


        if len(dots) > 2:  #Проверка на то что пользователь ввел две координаты
            print("Лишняя координата")
            continue

        if len(dots) < 2:  #Проверка на то что пользователь ввел две координаты
            print("Нехватает координат")
            continue

        x, y = dots

        if 0 > x or x > 2 or 0 > y or y > 2:  #Провекрка на попадание чисел в диапозон
            print("Введите числа от 1 до 2")
            continue

        if gamezone[x][y] != " ":  #Проверка на то что занята клетка или нет
            print("Клетка занята")
            continue
        return x, y

def name():  #Выдача игрокам имен
    name1 = input("Введите имя первого игрока-крестика")

    name2 = input("Введите имя второго игрока-нолика")

    return name2, name1

def win():  #Функция проверки выйгрыша
    win_gamezone = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),  #координты всех точек
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    cord = []  #Список куда будем класть проверяемые точки,для последущей проверки того что все 3 точки это кресты или ноли
    for i in range(3):  #Проверка на комбо строк
        for j in range(3):
            cord.append(gamezone[i][j])
        if cord == ["X" ,"X", "X"]:
            print(f"Выйграл{name1}")
            return True
        if cord == ["0", "0", "0"]:
            print(f'Выйграл {name2}')
            return True

        for i in range(3):  #Проверка на комбо столбцов
            for j in range(3):
                cord.append(gamezone[j][i])
            if cord == ["X", "X", "X"]:
                print(f"Выйграл{name1}")
                return True
            if cord == ["0", "0", "0"]:
                print(f'Выйграл {name2}')
                return True

        for i in range(3):  #Проверка на комбо диогонали
            cord.append(gamezone[i][i])
        if cord == ["X", "X", "X"]:
            print(f"Выйграл{name1}")
            return True
        if cord == ["0", "0", "0"]:
            print(f'Выйграл {name2}')
            return True

        for i in range(3):  #Проверка на комбо  инверсивной диоганали
            cord.append(gamezone[i][2-i])
            if cord == ["X", "X", "X"]:
                print(f"Выйграл{name1}")
                return True
            if cord == ["0", "0", "0"]:
                print(f'Выйграл {name2}')
                return True


num = 0
name1, name2 = name()
while True:

        num += 1

        monic()

        if num % 2 == 1:  #Очередность хода
            print(f'Ходит {name1}')
        else:
            print(f"Ходит {name2}")

        x, y = move()

        if num % 2 == 1:  #Установка фишки привязанная к очередности хода
            gamezone[x][y] = "X"
        else:
            gamezone[x][y] = "0"

        if win():#Вызов проверки на выйгрыш
            break


        if num == 9:  #Условие для ничьий
            print("Победила дружба")
            break
