# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1
    b = 1
    i = 1
    while i < m:
        temp = a
        a = a + b
        b = temp
        i +=1
        if i == n:
            element_n = a
        elif i == m:
            element_m = a
        else:
            continue
    return element_n, element_m

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = len(origin_list)
    count = 0
    while count < n:
        count += 1
        b = 0
        while b < n-1:     
            if origin_list[b] >  origin_list[b+1]: 
                origin_list[b], origin_list[b+1] = origin_list[b+1], origin_list[b]
            b += 1
    return origin_list  

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def new_filter(param, iterable):
    new_iterable = []
    for i in iterable:
        if i == param:
            new_iterable.append(i)
        else:
            continue
   
    return new_iterable            

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.