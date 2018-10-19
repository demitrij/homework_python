# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def kvadrat(list1):
    new_list = [i ** 2 for i in list1]
    return new_list
 
 
print(kvadrat([1,3,5,4,7,2,11]))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
def morefruits(fruit1, fruit2):
    new_fruit = [x for x in fruit1 if x in fruit2]
    return new_fruit
 
print(morefruits(['apple', 'banana', 'cherry', 'pineapple', 'orange', 'strawberry', 'melon'], ['apple','grape', 'orange', 'banana', 'kiwi', 'coconut']))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def element(el):
    new_element = [x for x in el if x >0 and x % 3 == 0 and x % 4 != 0]
    return new_element
 
print(element([-1, 6, 8, -6, 12, 9]))