'''
Created on 28 окт. 2018 г.

@author: Дмитрий
'''

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

start = input('To start game press 1')

digits = [ i  for i in range(1,91)]

    
def generator():                        #  генерируем карточки для игроков
    card = []
    alpha = []
    alpha = digits[:]  
    for i in range(0,3):
        
        t_list = [" "," "," "," "]
        a = 5
        while a > 0:
            a -= 1
            choice = random.choice(alpha)
            alpha.remove(choice)
            t_list.append(choice)
            random.shuffle(t_list)
            
        card.append(t_list)  
        
    return card
    
def player_card(p_card):                              # отрисовываем карточку игрока        
    print('----------------- Игрок ----------------')
    for i in p_card:
        print(i)
    
    print ('----------------------------------------')
    return p_card
    
def comp_card(c_card):                                  # отрисовываем карточку компьютера
    print('--------------- Компьютер --------------')
    for i in c_card:
        print(i)
    
    print ('----------------------------------------')
    return c_card   

def game():
    beta = []
    beta = digits[:]
    card1 = generator()
    p_card = player_card(card1)
    card2 = generator()
    c_card = comp_card(card2)
    player_status = 15
    comp_status = 15
    win = False
    global winner
    winner = None
    
    while win == False:
        p_number = False

        choice = random.choice(beta)
        beta.remove(choice)
        str_choice = 'Выпало %s ' % choice 
        print (str_choice)
        cross_out = input('Желаете зачеркнуть число? y/n ')
 
        for i in p_card:                                    # проверяем наличие числа в карточке
            if choice in i:
                p_number = True
        if cross_out == 'y' and p_number == True:
            for row in p_card:
                try:
                    x = row.index(choice)
                    row[x] = '*'
                    player_status -= 1
                    p_card = player_card(p_card)
                except:
                    continue
        elif cross_out == 'y' and p_number == False:
            p_card = player_card(p_card)
            print('Игра проиграна')
            win = True
            winner = 'Computer win'
        elif cross_out == 'n' and p_number == True:
            p_card = player_card(p_card)
            print('Игра проиграна')
            win = True
            winner = 'Computer win'
        else:
            p_card = player_card(p_card)        
           
            
        
        for i in c_card:               #
            if choice in i:
                for row in c_card:
                    try:
                        x = row.index(choice)
                        row[x] = '*'
                        comp_status -= 1
                        
                    except:
                        continue 
                      
           
                
                
                
       
        c_card = comp_card(c_card)
        
        if player_status == 0:
            
            win = True
            winner = "Player win"
            break
        elif comp_status == 0:
            
            win = True
            winner = 'Computer win'
            break
        else:
            continue
    return winner
                
        
game()    
print(winner)  