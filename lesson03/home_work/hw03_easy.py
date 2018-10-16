# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    a = int(number * (10 ** (ndigits + 1)))
    if a % 10 >= 5:
        while a % 10 != 0:
            a += 1
        a = a / (10 ** (ndigits + 1))
    else:
        while a % 10 != 0:
            a -= 1
        a = a / (10 ** (ndigits + 1))
    return(a)



print(my_round(2.1234567, 3))
print(my_round(2.1949967, 4))
print(my_round(2.9999364, 6))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = int(str(ticket_number)[0:3])
    b = int(str(ticket_number)[3:])

    def summa(x):
        sum_x = 0
        while x % 10 != 0:
            sum_x += x % 10
            x = x // 10
        return sum_x

    sum_a = summa(a)
    sum_b = summa(b)

    if sum_a == sum_b:
        return True
    else:
        return False


print("\n")
print(lucky_ticket(123016))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
