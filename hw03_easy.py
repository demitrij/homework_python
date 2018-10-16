# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    temp = str(number)
    a = temp.split(".")
    b = a[1]
    substr = len(b) - ndigits
    d =temp[-substr:]
    e = "5" + "0" * (substr -1)
    c = "0." + "0" * (ndigits - 1) + "1"
    new_digit = temp[:-substr]
    
    if int(e) <= int(d):
        f = float(new_digit) + float(c) 
    else:    
        f = number
    return f   
        

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = str(ticket_number)
    tiket = []
    for i in a:
        tiket.append(int(a))
    part1 = sum(tiket[0:3])
    part2 = sum(tiket[3:])
    if part1 == part2:
        return "Билет счастливый"
    else:
        return "Обычный билет"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))