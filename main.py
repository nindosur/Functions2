    # 1
#def f(n, b, dell):
#     if n % dell == 0 and b % dell == 0:
#         if dell > min(n, b):
#             return dell(n, b, dell+1)
#         else:
#             return dell
#     else:
#         if dell > min(n, b):
#             return dell(n, b, dell+1)

# def f(n, b):
#     if b == 0:
#         return n
#     else:
#         return f(b, b%n)
#
# n = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# dell = 2
# f(b, b%n)
# print("Наибольший общий делитель двух целых чисел:", f(b, b%n))

    # 2
# import random
# skot = []
# score = 0
# for i in range(4):
#     skot.append(str(random.randint(0, 9)))
# print(skot)
#
# def SkotniyDvor(skot, score):
#     c = 0
#     b = 0
#     count = 0
#     while True:
#         c = 0
#         b = 0
#         print("Быки - сколько цифр числа угадано; \n"
#               "Коровы - сколько цифр угадано и стоит на нужном месте.")
#         n = input("Введите 4х значное число: ")
#         count += 1
#         for i in range(4):
#             if skot[i] == n[i]:
#                 c+=1
#             elif (n[i] in skot):
#                 b += 1
#         if c == 4:
#             print("Быков", b)
#             print("Коров", c)
#             print("Кол-во ходов", count)
#             break
#         print("Быков", b)
#         print("Коров", c)
# SkotniyDvor(skot, score)

    # 3
# # N = 8 # N - длина доски (N*N)
# # Посещение нужно для того, чтобы:
# # 1. Хранить список посещений фигуры
# # 2. Хранить клетки для возможного хода коня
# visited = [[0 for i in range(N)] for y in range(N)]
# pos = 1
# # Клетки из 8ми вариаций посещения коня
# row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
# col = [1, 2, 2, 1, -1, -2, -2, -1, 1]
#
# # проверка является ли (х, у) правильными координатами доски
# def isvalid(x,y):
#     return not (x < 0 or y < 0 or x >= N or y >= N)
#
# # вместо нулей можем передать любую начальную позицию для x и y
# def horse(visited, x, y, pos):
#     visited[x][y] = pos
#     if pos >= N*N:
#         for i in visited:
#             print(i)
#         print()
#         visited[x][y] = 0
#         return
#     # проверка всех возможных ходов
#     for j in range(8):
#         # новая позиция коня из текущей клетки
#         newX = x + row[j]
#         newY = y + col[j]
#         if isvalid(newX, newY) and visited[newX][newY] == 0:
#             horse(visited, newX, newY, pos+1)
#     visited[x][y] = 0
#
# isvalid(0,0)
# horse(visited, 0, 0, pos)

    # 4
from random import *
    # Пятнашки

list1 = [i for i in range(10)]
list1 = sorted(list1, reverse=True)
n = randint(1,9)
list1[n] = 0
print("Начинать игру будем с позиции: ", n)

# вывод на экран
def printP(list1):
    print('*'*13)
    for i in range(3):
        print('|' , list1[0+i*3] , '|' , list1[1+i*3] , '|' , list1[2+i*3] , '|' )
        print('*'*13)

# правила игры
def pravila():
    print('Управление: \n Ввод w - ход вверх;\n Ввод s - ход вниз;\n Ввод a - ход влево;\n Ввод d - ход вправо; ')
    print('Победа будет, если все ячейки будут стоять на своем месте.')
    print('Удачной игры!')

# процесс игры
def game(list1, n):
    pravila()
    list2 = sorted(list1, reverse=True)
    while (list1 != list2):
        printP(list1)
        input_walk = input("Введите текущий ход: ")
        if (input_walk == 'w'):
            if n not in (0, 1, 2):
                list1[n], list1[n-3] = list1[n-3], list1[n]
                n = n - 3
            else:
                print('Некорректный ввод. Нельзя двигаться вверх за границу.')
        elif (input_walk == 's'):
            if n not in (6, 7, 8):
                list1[n], list1[n + 3] = list1[n + 3], list1[n]
                n = n + 3
            else:
                print('Некорректный ввод. Нельзя двигаться вниз за границу.')
        elif (input_walk == 'a'):
            if n not in (0, 3, 6):
                list1[n], list1[n - 1] = list1[n - 1], list1[n]
                n = n - 1
            else:
                print('Некорректный ввод. Нельзя двигаться влево за границу.')
        elif (input_walk == 'd'):
            if n not in (2, 5, 8):
                list1[n], list1[n + 1] = list1[n + 1], list1[n]
                n = n + 1
            else:
                print('Некорректный ввод. Нельзя двигаться вправо за границу.')
        else:
            print('Некорректный ввод. Для движения используйте W A S D')

game(list1, n)