# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create(name):
    k = 1
    while k < 10:
        part = "_ %s" % str(k)    
        dir_name = name + part
    
        k += 1
        p = os.getcwd()
        os.mkdir(dir_name, mode = 0o777)
create("dir")
g = input()

def delete (name):
    k = 1
    while k < 10:
        part = "_ %s" % str(k)    
        dir_name = name + part
    
        k += 1
        os.rmdir(dir_name)
delete("dir")



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def lister():
    directories = [] 
    list_dir = os.listdir(path = '.')
    for i in list_dir:
        if os.path.isdir(i):
            directories.append(i)
    return directories
print(lister())



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# этот код необходимо встаить в файл для его копирования

import newlib
import sys

name = sys.argv[0]

newlib.copy(name)


# данный код выполняет копирование файла. Код находиться в файле newlib.py 
def copy(file):
    f = open(file, 'r') 
    text = f.read()
    new_text = text[:]
    t_name = file.split('.')
    new_name = t_name[0] + '(copy).'+ t_name[1]
    new_file = open(new_name, 'tw')
    new_file.write(new_text)
    f.close()
    new_file.close()

    
