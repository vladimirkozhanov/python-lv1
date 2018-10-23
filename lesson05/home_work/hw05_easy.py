# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
from shutil import copy

def dirmaker19():
    i = 1
    while i < 10:
        dir_path = os.path.join(os.getcwd(), "NewDir" + str(i))
        try:
            os.makedirs(dir_path)
            print("Создана директория", dir_path)
        except FileExistsError:
            print("Такая директория существует.")
            break
        i += 1





def dirremover19():
    i = 5               # удаляю не все папки, чтобы следующему скрипту было, что показать.
    while i < 10:
        dir_path = os.path.join(os.getcwd(), "NewDir" + str(i))
        try:
            os.rmdir(dir_path)
            print("Удалена директория", dir_path)
        except FileNotFoundError:
            print("Такая директория не найдена.")
            break
        i += 1






# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def sh_dir():
    a =[]
    print("Список директорий:")
    for x in os.listdir():
        if os.path.isdir(x):
            a.append(x)
    print(a)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def cop_file():
    file_name = (os.path.split(sys.argv[0]))
    copy(sys.argv[0], "copy " + file_name[1])


# ункции для задания normal:

def dirmake(dir_name):
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.makedirs(dir_path)
            print("Создана директория", dir_path)
        except FileExistsError:
            print("Такая директория существует.")


def dirremove(dir_name):

        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.rmdir(dir_path)
            print("Удалена директория", dir_path)
        except FileNotFoundError:
            print("Такая директория не найдена.")

def chadir(dir_name):
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.chdir(dir_path)
            print("Перешли в директорию", dir_path)
        except FileNotFoundError:
           print("Такая директория не найдена.")