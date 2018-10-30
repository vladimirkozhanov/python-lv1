#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import math


def lineIN():
    a = []
    q = False
    a.append(random.randint(1, 89))
    while len(a) != 5:
        x = random.randint(1, 89)
        for i in a:
            if i // 10 == x // 10 or x in a:
                q = True
            else:
                continue
        if q == False:
            a.append(x)
            a.sort()
        else:
            q = False
    return a

def kartochka(a, gnumbers):
    i = 0
    q = False
    while i < 3:
        x = lineIN()
        for j in gnumbers:
            if j in x:
                q = True
            else:
                continue
        if q == False:
            a.append(x)
            gnumbers += x
            gnumbers.sort()
        else:
            q = False
            continue
        i += 1
    return a, gnumbers

def transforma(a):
    for i in range(len(a)):
        k = 0
        while k < 8:
            try:
                if math.floor(a[i][k] / 10) == k:
                    k += 1
                    continue
                else:
                    a[i].insert(k, 91)
                    k += 1

            except IndexError:
                a[i].append(91)

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 91:
                a[i][j] = " "

    return(a)


a = []
b = []
gnumbers = []

kartochka(a, gnumbers)
kartochka(b, gnumbers)


print("\n Уникальные номера (для тестов):", gnumbers)
print("\n")
'''for x in a: #это карточки до добавления пробелов на пустых разрядах
    print(x)
print("\n")
for x in b:
    print(x)
print("\n")'''

transforma(a)
transforma(b)



gnumbers = []

i = 0
while i < 89:
    while True:
        n = random.randint(1, 89)
        if n in gnumbers:
            continue
        else:
            gnumbers.append(n)
            break
    print("Карточка пользователя:")
    for x in a:
        print(x)
    print("\n")

    print("Карточка соперника:")
    for x in b:
        print(x)
    print("\n")
    print("Бочонок №", n)
    answer = input("Зачеркнуть цифру? (y/n):")
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == n and answer == "y":
                print("Следующий ход.")
            elif a[i][j] == n and answer == "n":
                print("Вы проиграли.")
            elif a[i][j] != n and answer == "n":
                print("Следующий ход.")

