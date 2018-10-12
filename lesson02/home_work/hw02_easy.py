# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()


fruits = ["яблоко", "груша", "дыня", "апельсин", "банан"]

i = 1
for fr in fruits:
    print('{}{:>10}'.format(i, fr))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 3, 4, 5]

i = 0
while i < len(a): #с "for-in" это не заработало, потому что цикл пропускал следующий элемент после удаленного
    for y in b:
        if y == a[i]:
            a.remove(a[i])
    i += 1
print("\n", a, "\n")



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

cshisla = [1, 2, 3, 4, 5, 6, 7]
new_cshisla = []
for i in cshisla:
    if i % 2 == 0:
        new_cshisla.append(i / 4)
    else:
        new_cshisla.append(i * 2)

print(new_cshisla)

