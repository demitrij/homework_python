import os, sys

def dir_change(path):
    
    try:
        os.chdir(path)
        print('Успешно перешел')
    except:
        print('Переход не удался')

def dir_del(path):
    try:
        os.rmdir(path)
        print('папка удалена')
    except:
        print('удаление не удалось')

def dir_create(path):        
    try:
        os.mkdir(path, mode = 0o777)
        print('папка создана')
    except:
        print('не удалось создать папку')