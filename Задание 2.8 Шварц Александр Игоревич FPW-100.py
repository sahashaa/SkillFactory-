from random import randint
#Класс точки
class Dot:
    def __init__(self,x,y):
        self.gor=x#горизонт координата
        self.ver=y#вертикал координата
    def __eq__(self,other): #переопределяем == т.к обычное == не работает ,т.к в наших точках две координаты,все остальные методы,например count сравнения тоже будут работать с его поддержкой
       return self.gor==other.x and self.ver==other.ver##создаем self куда будет вставляется начальная переменная а рядом,"под каким" методом она будет ,для other тоже самое

    def __repr__(self):#Используем этот "магический" метод так как создания "простого метода" дает адрес ячейки памяти но не печатает саму строку
        return f"Dot({self.gor}, {self.ver})"
    #Можете пожалуйста обьяснить почему вот такой код работает а этот не работает
        #  def Printdot(self):
        #       return f'Dot({self.gor}:{self.ver})'

#Классы исключений


class Bexp(Exception):#Родительский класс для исключений#а также супер родительский клас предусмотренный питоном
        pass

class OutBexp(Bexp):#исключение если игрок делает ход вне поля
    def __str__(self):
        return "Выстрел вне боевых действий"

class UsedBexp(Bexp):#Исключение если игрок ставит точку в уже использованное место
    def __str__(self):
        return "Вы уже стреляли в эту точку"

#Класс корабль

class Ship:#класс корабля

    def __init__(self,bow,axis,lenght):#конструктор класса куда мы добавляем свойства класса
        self.bow=bow#начало корабля,стартовая его точка,можно сказть его нос
        self.axis = axis#орентация корабля в пространстве,задавая ноль мы подрузомеваем что корабль "плывет" горизонтально а если 1 то вертикально
        self.l=lenght#длина корабля,используется для того чтобы цикл знал сколько точек нужно отрисовать
        self.lenght=lenght

    def dots(self):
        ship_dots=[]#наш корабль
        for i in range(self.l):#даем циклу число(находящиеся в свойствах,говорящее какой длины корабль)которое указывает сколько нужно "закрасить" клеток от носа корабля
            ax_x=self.bow.gor#задаем перменную  к которой будем прибавлять точки для отрисовки точек по горионтали
            ax_y=self.bow.ver#задаем переменную к которой будем прибавлять точки для отрисовки точек по вертикали

            if self.axis == 0:#спрашиваем как расположен наш корабль
                ax_x +=i#прибавляем к горизантальной линии

            elif self.axis == 1:#спрашиваем как расположен наш корабль
                ax_y+=i#прибавляем к вертикальной линии

            ship_dots.append(Dot(ax_x,ax_y))#наконецто создаем наш корабль
        return ship_dots
    def kill(self,hit):#метод попадания
        return hit in self.dots#возвращает булевое значение,проверка на то попали мы или нет, тоесть находиться ли хит в списке точек


    #Класс игрового поля
    class Board():
        def __init__(self,size=6,visible=False):
            self.sze=size#метод указывающий на размер доски
            self.vsb=visible#Видно доску или нет

            self.count=0

            self.field=[['0'] * size for _ in range(size)]#генератор списка,через который мы создаем саму доску

            self.busy=[]#метод в котором заложен список клеток в которых уже стоят корабли
            self.ships=[]#кординаты самих клеток где стоят корабли

        def __str__(self):#метод благодоря которму не надо будет постоянно вызывать принт
            board=""
            board+=" / 1 / 2 / 3 / 4 / 5 / 6 /"#просто шаблон верхней части доски
            for i,values in enumerate(self.field):#"генератор" доски через эну сначало достаем номер строки(i+1),номер этерации ,а затем само значение(values)\

                board+=f'\n{i+1} / ' + '/'.join(values) +'/'#первое это номер строки он просто идет через перенос строки,а значение строки мы разделяем слешем через джоин

            if self.vsb==1:#механизм скрытия поля
                board=board.replace('х','0')#Замена открыттых ячеек на скрытые
            return board
        def out(self,d):#метод для случаев когда точка или корабль находятьися вне поля
            return not(0 <= d.gor < self.size) and (0<=d.ver <self.size )



        def circle(self,ship,sing=False):#Обводка вокруг корабля
            near = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
            for d in ship.dots:
                for dx,dy in near:
                    cur=Dot(d.gor+dx,d.ver+dy)
                    if not(self.out(cur)) and cur not in self.busy:
                        if sing:
                            self.field[cur.gor][cur.ver] = '.'
                        self.busy.append(cur)

        def add_ship(self,ship):#Корабль на доске

            for d in ship.dots:
                if self.out(d) or d in self.busy:
                    raise OutBexp()
            for d in ship.dots:
                self.field[d.gor][d.ver]='$'
                self.busy.append(d)

                self.ships.append(ship)
                self.circle(ship)

        def shot(self,d):
            if self.out(d):
                raise OutBexp()

            if d in self.busy:
                raise UsedBexp()
            self.busy.append(d)

            for ship in self.ships:
                if d in ship.dots:
                    ship.lives -=1
                    self.field[d.gor][d.ver]
                    if ship.lives==0:
                        self.count+=1
                        self.circle(ship, sing == True)
                        print("Корабль затонул")
                    else:
                        print('Есть пробитие!')
                        return True
            self.field[d.gor][d.ver]='.'
            print("Не попал")
            return False

        def restart(self):
            self.busy=[]

            #Класс игрока
class Player:
    def __init__(self,board,enemy ):
        self.board = board
        self.enemy = enemy

    def pointer(self):
        raise error

    def move(self):
        while True:
            try:
                target = self.pointer()
                repeat = seld.enemy.shot(target)
                return repeat
            except Bexp as Y:
                print(Y)

class computer(Player):
    def random(self):
        d=Dot(randint(0,5),randint(0,5))
        print(f'Машина ходит сюда-{d.gor+1}{d.ver+1}')
        return d

class Human(Player):
    def Human_ask(self):
        while True:
            dots=input("Твой ход,человек").split()

            if len(dots)!=2:
                print("Введите две точки")
                continue

            a,b=dots

            if not (a.isdigit()) or not (b.isdigit()):
                print("Ввести можно только числа")
                continue

            a , b=int(a),int(b)

            return Dot(a-1,b-1)

class Game:
    def goboard(self):
        lens=[3,2,2,1,1,1,1]
        board=Board(size=self.size)
        attempts=0
        for l in lens:
            while True:
                attempts+=1
                if attempts>2000:
                    return None
                ship=Ship(Dot(randint(0,self.size),randint(0,self.size)),1,randint(0,self.size))
                try:
                    board.add_ship(ship)
                    break
                except Bexp:
                    pass
        board.restart()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.goboard()
        return board

    def __init__(self,size = 6):
        self.size = size
        ply = self.random_board()
        comp = self.random_board()
        comp.vsb = True

        self.cpm = computer(comp,ply)
        self.us = Human(ply,comp)

    def greet(self):
        print('****************************')
        print('  Здравствуй человек  ')
        print('  Добро пожаловать в  ')
        print("      МОРСКОЙ БОЙ     ")
        print('****************************')
        print('----------------------------')
        print('формат ввода: x y ')
        print(' x - номер строки ')
        print(' y - номер столбца ')

    def loop(self):
        num=0
        while True:
            print('-'*20)
            print('Доска игрока')
            print(self.us.board)
            print("-"*20)
            print('Доска машины')
            print(self.cpm.board)
            print('-'*20)
            if num % 2 == 0 :
                print("Ходи человек")
                repeat = self.us.move()
            else:
                print('Ходит машина')
                repeat = self.cpm.move()
            if repeat:
                num -=1

            if self.cpm.board.count == 7:
                print("-"*20)
                print('Человек победил')
                break

            if self.us.board.count == 7:
                print('-'*20)
                print('Машина одержала верх')
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()
        g=Game()
        g.start()